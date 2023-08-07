// Get a value of a given key from a link to json.

$(document).ready(function () {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.getJSON(url)
    .done(function (data) {
      const hello = data.hello;
      $('#hello').text(hello);
    })
    .fail(function () {
      $('#hello').text('error fetching content.');
    });
});
