import hashlib
import json
import os
import os.path

from constants import ALL, DEFAULT, FUNCTIONS, GROUPS, NUMBERS, OPERATIONS, OTHERS
from datetime import datetime
from flask import abort, Flask, jsonify, redirect, render_template, request


def get_data():
    if not os.path.exists("data.json"):
        return set_data({"last": "", "designs": []})

    with open("data.json", "r") as f:
        return json.load(f)


def set_data(data):
    with open("data.json", "w+") as f:
        json.dump(data, f, indent=4)

    return data


get_data()


app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.html")


@app.route("/github")
def github():
    return redirect("https://github.com/chamburr/calc-designer", code=302)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/app")
def _app():
    data = get_data()

    if len(data["designs"]) < 1:
        timestamp = datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
        id = str(int(hashlib.md5(timestamp.encode()).hexdigest()[:7], 16))

        data["last"] = id
        data["designs"].append(
            {
                "id": id,
                "name": "Default",
                "created": timestamp,
                "updated": timestamp,
                "details": DEFAULT,
            }
        )

        set_data(data)

    elif not data["last"]:
        data["last"] = data["designs"][0]["id"]

        set_data(data)

    item = [x for x in data["designs"] if x["id"] == data["last"]][0]
    all_items = [x for x in data["designs"] if x["id"] != data["last"]]

    return render_template(
        "app.html",
        item=item,
        all_items=all_items,
        all=ALL,
        numbers=NUMBERS,
        operations=OPERATIONS,
        functions=FUNCTIONS,
        others=OTHERS,
        groups=GROUPS,
    )


@app.route("/api")
def api():
    return "", 204


@app.route("/api/health")
def api_health():
    abort(418)


@app.route("/api/data", methods=["GET", "POST", "DELETE"])
def api_data():
    data = get_data()

    if request.method == "GET":
        for element in data["designs"]:
            del element["details"]

        return jsonify(data["designs"])

    elif request.method == "POST":
        name = request.form.get("name")

        if name is None or len(name) > 100:
            abort(400)

        timestamp = datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
        id = str(int(hashlib.md5(timestamp.encode()).hexdigest()[:7], 16))

        item = {
            "id": id,
            "name": name,
            "created": timestamp,
            "updated": timestamp,
            "details": DEFAULT,
        }

        data["last"] = id
        data["designs"].append(item)

        set_data(data)

        del item["details"]

        return jsonify(item)

    elif request.method == "DELETE":
        data["last"] = ""
        data["designs"].clear()

        set_data(data)

        return "", 204


@app.route("/api/data/<id>", methods=["GET", "PATCH", "DELETE"])
def api_data_id(id):
    data = get_data()
    item = next(iter([x for x in data["designs"] if x["id"] == id]), None)
    index = data["designs"].index(item) if item is not None else -1

    if item is None:
        abort(404)

    if request.method == "GET":
        data["last"] = item["id"]

        set_data(data)

        return jsonify(item)

    elif request.method == "PATCH":
        name = request.form.get("name")
        details = request.form.get("details")

        if name is None and details is None:
            abort(400)

        if name is not None:
            item["name"] = name

        if details is not None:
            try:
                details = json.loads(details)
            except json.decoder.JSONDecoderError:
                abort(400)

            if not isinstance(details, list):
                abort(400)

            for element in details:
                id = element.get("id")
                position = element.get("position")
                size = element.get("size")
                styles = element.get("styles")

                for key in element.keys():
                    if key not in ["id", "position", "size", "styles"]:
                        abort(400)

                if id not in [x.lower() for x in GROUPS + ALL]:
                    abort(400)

                if id in [x.lower() for x in ALL]:
                    if not isinstance(position, dict):
                        abort(400)

                    for key, value in position.items():
                        if key not in ["x", "y"] or not isinstance(value, int):
                            abort(400)

                    if not isinstance(size, dict):
                        abort(400)

                    for key, value in size.items():
                        if key not in ["width", "height"] or not isinstance(value, int):
                            abort(400)
                else:
                    element.pop("position", None)
                    element.pop("size", None)

                if not isinstance(styles, str):
                    abort(400)

            item["details"] = details

        item["updated"] = datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

        data["last"] = item["id"]
        data["designs"][index] = item

        set_data(data)

        return jsonify(item)

    elif request.method == "DELETE":
        if data["last"] == item["id"]:
            data["last"] = ""

        del data["designs"][index]

        set_data(data)

        return "", 204


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


app.run(host="127.0.0.1", port=8080, debug=True)
