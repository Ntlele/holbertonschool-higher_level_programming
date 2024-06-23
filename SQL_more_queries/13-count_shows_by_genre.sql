-- Select the genre from tv_genres and count the number of shows linked to each genre
-- Display the genre and the number of shows linked to that genre
-- Only show genres that have at least one show linked
-- Sort the results in descending order by the number of shows linked to each genre

SELECT tv_genres.genre AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
