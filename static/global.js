document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.navbar-burger').forEach(function (el) {
    el.addEventListener('click', function () {
      el.classList.toggle('is-active');

      document.getElementById(el.dataset.target).classList.toggle('is-active');
    });
  });

  document.querySelectorAll('.tabs ul li').forEach(function (el) {
    el.addEventListener('click', function () {
      this.parentElement.parentElement.querySelectorAll('.tabs ul li').forEach(function (el2) {
        el2.classList.remove('is-active');
      });

      this.parentElement.parentElement.querySelectorAll('.tab-content').forEach(function (el2) {
        el2.classList.remove('is-active');
      });

      this.classList.add('is-active');

      document.getElementById(this.getAttribute('data-target')).classList.add('is-active');
    });
  });
});
