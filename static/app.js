function showModal(title, description, buttonText, buttonStyle, cancel, callback, cancelCallback) {
  document.getElementById('modal-title').innerText = title;
  document.getElementById('modal-description').innerText = description;
  document.getElementById('modal-button').innerText = buttonText;
  document.getElementById('modal-button').classList.add('is-' + buttonStyle);
  document.getElementById('modal-cancel').style.display = cancel == false ? 'none': '';
  document.getElementById('modal').classList.add('is-active');

  document.getElementById('modal').addEventListener('click', function handler(event) {
    if (['modal-button', 'modal-close', 'modal-cancel', 'modal-background'].indexOf(event.target.id) < 0) {
      return;
    }

    document.getElementById('modal').removeEventListener('click', handler);

    if (event.target.id == 'modal-button' && callback) {
      event.target.classList.add('is-loading');
      callback();
    } else if (event.target.id != 'modal-button' && cancelCallback) {
      event.target.classList.add('is-loading');
      cancelCallback();
    }

    hideModal();
  });
}

function hideModal() {
  document.getElementById('modal-title').innerText = '';
  document.getElementById('modal-description').innerText = '';
  document.getElementById('modal-button').innerText = '';
  document.getElementById('modal-button').classList = ['button'];
  document.getElementById('modal-cancel').style.display = '';
  document.getElementById('modal-cancel').classList = ['button'];
  document.getElementById('modal').classList.remove('is-active');
}

function request(method, url, data, callback) {
  if (!data) data = {};

  data = Object.keys(data).map(function (key) {
    return encodeURIComponent(key) + '=' + encodeURIComponent(typeof data[key] == 'object' ? JSON.stringify(data[key]) : data[key]);
  }).join('&');

  if (method == 'GET' && data) {
    url = url + '?' + data;
    data = '';
  }

  fetch(url, {
    method: method,
    headers: data ? { 'Content-Type': 'application/x-www-form-urlencoded' } : {},
    body: data ? data : null,
  })
    .then(function (response) {
      if (response.status == 204) return {};
      return response.json();
    })
    .then(function (data) {
      if (callback) callback(data);
    })
    .catch(function (err) {
      showModal('Error', 'An unexpected error occurred. (' + err + ')', 'Ok', 'success', false);
    });
}

function currentDocument() {
  return document.getElementById('input-document').value;
}

function selectDocument() {
  request('GET', '/api/data/' + currentDocument(), {}, function () {
    window.location.reload();
  });
}

function createDocument() {
  var name = document.getElementById('input-name-new').value;

  if (!name) {
    showModal('Error', 'Please enter a valid name.', 'Ok', 'success', false);
    return;
  }

  request('POST', '/api/data', { name: name }, function () {
    window.location.reload();
  });
}

function saveDocument() {
  var name = document.getElementById('input-name').value;

  if (!name) {
    showModal('Error', 'Please enter a valid name.', 'Ok', 'success', false);
    return;
  }

  request('PATCH', '/api/data/' + currentDocument(), { name: name, details: state }, function(data) {
    window.location.reload();
  });
}

function deleteDocument() {
  showModal('Confirmation', 'Do you really want to delete this document?', 'Delete', 'danger', true, function () {
    request('DELETE', '/api/data/' + currentDocument(), {}, function (data) {
      window.location.reload();
    });
  });
}

function deleteDocumentAll() {
  showModal('Confirmation', 'Do you really want to delete everything? This will delete your documents.', 'Delete all', 'danger', true, function () {
    request('DELETE', '/api/data', {}, function (data) {
      window.location.reload();
    });
  });
}

function getElement(id) {
  var item = state.find(function (element) {
    return element.id == id;
  });

  if (!item) {
    if (groups.includes(id)) {
      state.push({ id: id, styles: '' });
    } else {
      state.push({ id: id, position: { x: 0, y: 0 }, size: { width: 0, height: 0 }, styles: '' });
    }

    return getElement(id);
  }

  return item;
}

function currentElement() {
  return getElement(document.getElementById('input-element').value);
}

function selectElement() {
  var element = currentElement();

  if (element.position && element.size) {
    document.getElementById('label-position').style.display = '';
    document.getElementById('input-position').style.display = '';
    document.getElementById('label-size').style.display = '';
    document.getElementById('input-size').style.display = '';
    document.getElementById('input-position').value = 'X: ' + element.position.x + ', Y: ' + element.position.y;
    document.getElementById('input-size').value = 'Width: ' + element.size.width + ', Height: ' + element.size.height;
  } else {
    document.getElementById('label-position').style.display = 'none';
    document.getElementById('input-position').style.setProperty('display', 'none', 'important');
    document.getElementById('label-size').style.display = 'none';
    document.getElementById('input-size').style.setProperty('display', 'none', 'important');
  }

  document.getElementById('input-styles').value = element.styles;
}

function saveElement() {
  var element = currentElement();

  element.styles = document.getElementById('input-styles').value;

  renderElement();
}

function renderElement() {
  var styles = [];

  for (let element of state) {
    if (element.styles) {
      var selector = element.id == 'all' ? '.design-element' : groups.includes(element.id) ? '.design-element-' + element.id : '.design-element[data-id="' + element.id + '"]';
      var style = element.styles.replace('\n', ' ').split('}')[0].split('<')[0];

      styles.push('<style>' + selector + '{' + style + '}</style>');
    }

    if (!groups.includes(element.id)) {
      var el = document.querySelector('.design-element[data-id="' + element.id + '"]');
      var bounding = document.getElementById('design-content').getBoundingClientRect();

      el.style.left = Math.round(element.position.x / 2360 * bounding.width) + 'px';
      el.style.top = Math.round(element.position.y / 1640 * bounding.height) + 'px';
      el.style.width = Math.round(element.size.width / 2360 * bounding.width) + 'px';
      el.style.height = Math.round(element.size.height / 1640 * bounding.height) + 'px';
    }
  }

  document.getElementById('design-styles').innerHTML = styles.join('\n');
}

document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.design-element').forEach(function (el) {
    el.addEventListener('click', function (event) {
      document.getElementById('input-element').value = el.getAttribute('data-id');
      selectElement();
    });

    el.addEventListener('mousedown', function (event) {
      var bounding = document.getElementById('design-content').getBoundingClientRect();
      var size = el.getBoundingClientRect();

      if (event.clientX - bounding.x - el.style.left.slice(0, -2) - size.width > -20 && event.clientY - bounding.y - el.style.top.slice(0, -2) - size.height > -20) {
        return;
      }

      el.classList.add('is-dragging');

      function moveHandler(event) {
        if (!el.classList.contains('is-dragging')) return;

        var bounding = document.getElementById('design-content').getBoundingClientRect();
        var size = el.getBoundingClientRect();

        var left = event.clientX - bounding.x - size.width / 2;
        var top = event.clientY - bounding.y - size.height / 2;

        if (left < 0) left = 0;
        else if (left > bounding.width - size.width) left = bounding.width - size.width;

        if (top < 0) top = 0;
        else if (top > bounding.height - size.height) top = bounding.height - size.height;

        el.style.left = left + 'px';
        el.style.top = top + 'px';

        window.getSelection().removeAllRanges();
      }

      document.body.addEventListener('mousemove', moveHandler);
      document.body.addEventListener('mouseup', function handler() {
        el.classList.remove('is-dragging');

        var element = getElement(el.getAttribute('data-id'));
        var bounding = document.getElementById('design-content').getBoundingClientRect();

        element.position.x = Math.round(parseInt(el.style.left.slice(0, -2)) / bounding.width * 2360);
        element.position.y = Math.round(parseInt(el.style.top.slice(0, -2)) / bounding.height * 1640);

        document.body.removeEventListener('mouseup', handler);
        document.body.removeEventListener('mousemove', moveHandler);
      });
    });

    new ResizeObserver(function () {
      var element = getElement(el.getAttribute('data-id'));
      var bounding = document.getElementById('design-content').getBoundingClientRect();
      var size = el.getBoundingClientRect();

      element.size.width = Math.round(size.width / bounding.width * 2360);
      element.size.height = Math.round(size.height / bounding.height * 1640);
    }).observe(el);
  });

  window.addEventListener('resize', function() {
    renderElement();
  });

  selectElement();
  renderElement();

  document.querySelector('li[data-target="tab-document"]').addEventListener('click', function () {
    localStorage.setItem('activeTab', 'document');
  });

  document.querySelector('li[data-target="tab-styles"]').addEventListener('click', function () {
    localStorage.setItem('activeTab', 'styles');
  });

  var activeTab = localStorage.getItem('activeTab');
  if (activeTab && activeTab == 'styles') {
    document.querySelector('li[data-target="tab-document"]').classList.remove('is-active');
    document.querySelector('li[data-target="tab-styles"]').classList.add('is-active');
    document.getElementById('tab-document').classList.remove('is-active');
    document.getElementById('tab-styles').classList.add('is-active');
  }
});
