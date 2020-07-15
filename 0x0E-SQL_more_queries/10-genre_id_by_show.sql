-- all the genres by shows
SELECT t.title, s.genre_id FROM tv_shows t,tv_show_genres s WHERE t.id = s.show_id ORDER BY t.title,s.genre_id ASC;
