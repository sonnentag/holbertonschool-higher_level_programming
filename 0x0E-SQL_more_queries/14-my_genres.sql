-- list genres for TV show Dexter
SELECT t.name FROM tv_genres t JOIN tv_show_genres g ON t.id = g.genre_id JOIN tv_shows s ON g.show_id = s.id WHERE s.title = "Dexter";
