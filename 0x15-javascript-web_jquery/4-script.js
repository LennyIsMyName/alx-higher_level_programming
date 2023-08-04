$(document).ready(function () {
  const clk = $('#toggle_header');
  const head = $('header');
  clk.click(function () {
    head.toggleClass('red green');
  });
});
