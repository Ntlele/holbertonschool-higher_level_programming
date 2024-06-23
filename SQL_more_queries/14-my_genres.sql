-- Select the genre names of the show "Dexter" from the hbtn_0d_tvshows database
-- Join the tv_genres, tv_show_genres, and tv_shows tables based on their IDs
-- Filter the results to only show genres for the show "Dexter" by matching the show title
-- Sort the results in ascending order by the genre name

SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
