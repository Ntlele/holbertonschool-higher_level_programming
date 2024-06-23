-- Select tv_shows.title and tv_show_genres.genre_id for all shows in the hbtn_0d_tvshows database
-- Use LEFT JOIN to include shows that don't have a genre linked
-- Display 'NULL' if a show doesn't have a genre
-- Sort the results in ascending order by tv_shows.title and tv_show_genres.genre_id

SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, 'NULL') AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, genre_id ASC;
