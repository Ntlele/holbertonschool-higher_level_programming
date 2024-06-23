-- Select tv_shows.title and tv_show_genres.genre_id for shows with at least one genre linked in the hbtn_0d_tvshows database
-- Join the tv_shows and tv_show_genres tables on the show_id and id columns
-- Sort the results in ascending order by tv_shows.title and tv_show_genres.genre_id

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
