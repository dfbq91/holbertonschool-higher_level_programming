/* Fetches and list in list_movies tag
a list of star wars movies from swapi */
$.get('https://swapi-api.hbtn.io/api/films/?format=json',
  function (data) {
    for (const movie of data.results) {
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    }
  });
