-- list all shows  from database
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows RIGHT JOIN tv_show_genres WHERE genre IS NOT NULL ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
