$(document).ready(function () {
  const updater = $('#update_header');
  const element = $('header');
  updater.click(function () {
    element.text('New Header!!!');
  });
});
