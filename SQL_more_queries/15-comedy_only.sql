-- Select the title of Comedy shows from the hbtn_0d_tvshows database
-- Join the tv_shows, tv_show_genres, and tv_genres tables based on their IDs
-- Filter the results to only show Comedy shows by matching the genre name 'Comedy'
-- Sort the results in ascending order by the show title

SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
