-- all the genres, all the shows
SELECT t.title, s.genre_id FROM tv_shows t JOIN tv_show_genres s ON t.id = s.show_id ORDER BY t.title, s.genre_id ASC;
