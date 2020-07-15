-- list shows that aren't comedy 
SELECT t.title FROM tv_shows t WHERE t.title NOT IN (
SELECT t.title FROM tv_shows t JOIN tv_show_genres s ON t.id = s.show_id JOIN tv_genres g on g.id = s.genre_id WHERE g.name = "Comedy"
) ORDER BY t.title ASC;
