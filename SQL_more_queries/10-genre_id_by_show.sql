-- import the database dump from table to ur mysql server
SELECT tv_shows.title, tv_show_genres.genres.id FROM
tv_shows RIGHT JOIN tv_shows_genres ON tv_shows_genres.show.id=tv_show.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
