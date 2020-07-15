-- counts of shows in each genre.
SELECT g.name AS genre, count(*) AS number_of_shows FROM tv_show_genres t, tv_genres g WHERE t.genre_id = g.id GROUP BY t.name ORDER BY number_of_shows DESC;
