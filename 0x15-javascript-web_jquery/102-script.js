$(document).ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    $.get(url, { lang: languageCode }, function (data) {
      $('#hello').html(data.hello);
    });
  });
});
