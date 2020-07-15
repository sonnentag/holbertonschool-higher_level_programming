-- NULL genre ID
SELECT t.title, s.genre_id FROM tv_shows t LEFT JOIN tv_show_genres s ON t.id = s.show_id WHERE s.genre_id IS NULL ORDER BY t.title, s.genre_id ASC;
