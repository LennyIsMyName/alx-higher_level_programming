$(document).ready(function () {
  const clk = $('#red_header');
  const head = $('header');
  clk.click(function () {
    head.addClass('red');
  });
});
