-- Select tv_shows.title and tv_show_genres.genre_id for shows in hbtn_0d_tvshows without a genre linked
-- Use LEFT JOIN to include all shows from tv_shows table
-- Filter the results to show records where genre_id is NULL
-- Sort the results in ascending order by tv_shows.title and tv_show_genres.genre_id

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
