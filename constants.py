NUMBERS = [
    ".",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

OPERATIONS = [
    "+",
    "-",
    "=",
    "×",
    "÷",
]

FUNCTIONS = [
    "%",
    "(",
    ")",
    "⁺⁄₋",
    "¹⁄ₓ",
    "10ˣ",
    "2ⁿᵈ",
    "²√x",
    "³√x",
    "AC",
    "cos",
    "cosh",
    "e",
    "EE",
    "eˣ",
    "ln",
    "log₁₀",
    "m+",
    "m-",
    "mc",
    "mr",
    "Rad",
    "Rand",
    "sin",
    "sinh",
    "tan",
    "tanh",
    "x!",
    "x²",
    "x³",
    "xʸ",
    "ʸ√x",
    "π",
]

OTHERS = [
    "Result",
]

ALL = [
    *OTHERS,
    *NUMBERS,
    *OPERATIONS,
    *FUNCTIONS,
]


GROUPS = [
    "All",
    "Numbers",
    "Operations",
    "Functions",
]

DEFAULT = [
    {
        "id": "all",
        "styles": "align-items: center;\nborder: 2px solid #424344;\ncolor: #f5f5f5;\ndisplay: flex;\nfont-size: 24px;\nfont-weight: 500;\njustify-content: center;\ntext-align: center;\n"
    },
    {
        "id": ".",
        "position": {
            "x": 1880,
            "y": 1417
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "0",
        "position": {
            "x": 1410,
            "y": 1417
        },
        "size": {
            "width": 478,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "1",
        "position": {
            "x": 1410,
            "y": 1202
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "2",
        "position": {
            "x": 1645,
            "y": 1202
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "3",
        "position": {
            "x": 1880,
            "y": 1202
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "4",
        "position": {
            "x": 1410,
            "y": 987
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "5",
        "position": {
            "x": 1645,
            "y": 987
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "6",
        "position": {
            "x": 1880,
            "y": 987
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "7",
        "position": {
            "x": 1410,
            "y": 772
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "8",
        "position": {
            "x": 1645,
            "y": 772
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "9",
        "position": {
            "x": 1880,
            "y": 772
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "+",
        "position": {
            "x": 2115,
            "y": 1202
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "-",
        "position": {
            "x": 2115,
            "y": 987
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "=",
        "position": {
            "x": 2115,
            "y": 1417
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "\u00d7",
        "position": {
            "x": 2115,
            "y": 772
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "\u00f7",
        "position": {
            "x": 2115,
            "y": 557
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "%",
        "position": {
            "x": 1880,
            "y": 557
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "(",
        "position": {
            "x": 0,
            "y": 557
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": ")",
        "position": {
            "x": 235,
            "y": 557
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "\u207a\u2044\u208b",
        "position": {
            "x": 1645,
            "y": 557
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "\u00b9\u2044\u2093",
        "position": {
            "x": 0,
            "y": 987
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "10\u02e3",
        "position": {
            "x": 1175,
            "y": 772
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "2\u207f\u1d48",
        "position": {
            "x": 0,
            "y": 772
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "\u00b2\u221ax",
        "position": {
            "x": 235,
            "y": 987
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "\u00b3\u221ax",
        "position": {
            "x": 470,
            "y": 987
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "ac",
        "position": {
            "x": 1410,
            "y": 557
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "cos",
        "position": {
            "x": 470,
            "y": 1202
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "cosh",
        "position": {
            "x": 470,
            "y": 1417
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "e",
        "position": {
            "x": 940,
            "y": 1202
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "ee",
        "position": {
            "x": 1175,
            "y": 1202
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "e\u02e3",
        "position": {
            "x": 940,
            "y": 772
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "ln",
        "position": {
            "x": 940,
            "y": 987
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "log\u2081\u2080",
        "position": {
            "x": 1175,
            "y": 987
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "m+",
        "position": {
            "x": 705,
            "y": 557
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "m-",
        "position": {
            "x": 940,
            "y": 557
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "mc",
        "position": {
            "x": 470,
            "y": 557
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "mr",
        "position": {
            "x": 1175,
            "y": 557
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "rad",
        "position": {
            "x": 0,
            "y": 1417
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "rand",
        "position": {
            "x": 1175,
            "y": 1417
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "sin",
        "position": {
            "x": 235,
            "y": 1202
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "sinh",
        "position": {
            "x": 235,
            "y": 1417
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "tan",
        "position": {
            "x": 705,
            "y": 1202
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "tanh",
        "position": {
            "x": 705,
            "y": 1417
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "x!",
        "position": {
            "x": 0,
            "y": 1202
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "x\u00b2",
        "position": {
            "x": 235,
            "y": 772
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "x\u00b3",
        "position": {
            "x": 470,
            "y": 772
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "x\u02b8",
        "position": {
            "x": 705,
            "y": 772
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "\u02b8\u221ax",
        "position": {
            "x": 705,
            "y": 987
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "\u03c0",
        "position": {
            "x": 940,
            "y": 1417
        },
        "size": {
            "width": 241,
            "height": 221
        },
        "styles": ""
    },
    {
        "id": "result",
        "position": {
            "x": 0,
            "y": 0
        },
        "size": {
            "width": 2358,
            "height": 561
        },
        "styles": "align-items: flex-end;\nbackground-color: #424344;\nfont-size: 48px;\nfont-weight: 300;\njustify-content: flex-end;\npadding-right: 0.4em;\npadding-bottom: 0.2em;"
    },
    {
        "id": "functions",
        "styles": "background-color: #555556;"
    },
    {
        "id": "operations",
        "styles": "background-color: #ff9e0b;\nfont-size: 32px;"
    },
    {
        "id": "numbers",
        "styles": "background-color: #717172;"
    }
]
