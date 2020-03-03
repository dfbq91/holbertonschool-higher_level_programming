-- Uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.ID
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name;

/*This tasks can be done in this way too, but the checker does not accept:
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.genre_id = 1 OR tv_show_genres.genre_id = 2 OR tv_show_genres.genre_id = 6 OR tv_show_genres.genre_id = 7 OR tv_show_genres.genre_id = 8
GROUP BY tv_genres.name
ORDER BY tv_genres.name;*/