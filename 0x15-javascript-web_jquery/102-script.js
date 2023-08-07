/* Use api to translate greetings */
$(document).ready(function () {
  $('#btn_translate').click(function () {
    const code = $('#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/hello/';

    $.getJSON(url, code, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
