-- Import the database dump from hbtn_0d_tvshows

SELECT tv_shows.title, IFNULL(tv_genres.name, 'NULL') AS genre_name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, genre_name ASC;
