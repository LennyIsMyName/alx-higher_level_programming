$(document).ready(function () {
  $('#add_item').click(function () {
    const item = '<li>item</li>';
    $('ul.my_list').append(item);
  });

  $('#remove_item').click(function () {
    $('ul.my_list li:last').remove();
  });

  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
