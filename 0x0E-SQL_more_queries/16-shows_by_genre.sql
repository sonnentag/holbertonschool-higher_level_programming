-- all shows by genre
SELECT t.title, g.name FROM tv_shows t JOIN tv_show_genres s ON t.id = s.show_id LEFT JOIN tv_genres g ON g.id = s.genre_id ORDER BY title, name ASC;
