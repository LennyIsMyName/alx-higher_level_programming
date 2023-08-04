$(document).ready(function() {
  const clk = $('#red_header');
  const head = $('header');
  clk.click(function() {
    head.css('color', '#FF0000');
  });
});
