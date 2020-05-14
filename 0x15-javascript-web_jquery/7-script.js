/* Fetches and replaces in character tag the
value of name key in a URL of this URL */
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json',
  function (data, textStatus) {
    $('DIV#character').text(data.name);
  });
