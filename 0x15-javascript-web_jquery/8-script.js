// gets json from url and adds new
// html elements with the parsed data

$(document).ready(function () {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const items = data.results;
    $.each(items, function (index, item) {
      const newItem = $('<li>' + item.title + '</li>');
      $('#list_movies').append(newItem);
    });
  });
});
