// get hello from api while importing in HEAD
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  $('DIV#hello').html(data.hello);
});
