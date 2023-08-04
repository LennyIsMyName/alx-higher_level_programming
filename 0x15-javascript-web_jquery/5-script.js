$(document).ready(function () {
  const add = $('#add_item');
  const list = $('.my_list');
  add.click(function () {
    const item = $('<li>item</li>');
    list.append(item);
  });
});
