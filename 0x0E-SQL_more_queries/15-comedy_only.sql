-- comedy shows only
SELECT t.title FROM tv_shows t JOIN tv_show_genres s ON t.id = s.show_id LEFT JOIN tv_genres g ON g.id = s.genre_id WHERE g.name = 'Comedy' ORDER BY title ASC;
