-- counts of shows in each genre.
SELECT g.name AS genre, count(*) AS number_of_shows FROM tv_show_genres t JOIN tv_genres g ON t.genre_id = g.id GROUP BY g.name ORDER BY number_of_shows DESC;
