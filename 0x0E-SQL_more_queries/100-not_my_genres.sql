-- list genres not attributed to Dexter
SELECT t.name FROM tv_genres t WHERE t.name NOT IN (
SELECT t.name FROM tv_genres t JOIN tv_show_genres g ON g.genre_id = t.id JOIN tv_shows s on g.show_id = s.id WHERE s.title = "Dexter"
) ORDER BY t.name ASC;
