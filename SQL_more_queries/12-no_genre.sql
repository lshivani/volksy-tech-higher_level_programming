-- show in acsending order
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows AND tv_show_genres ORDER BY tv_shows.title ASC,tv_show_genres.genre_id ASC;
