/* Display the value of hello (a key) in the
hello tag once head have been imported */
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
      $('DIV#hello').text(data.hello);
});
