-- show  one record named with dexter , ascending 
SELECT tv_genres.name,FROM tv_genres JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_show_genres_show_id = tv_shows.id WHERE tv_shows.title='Dexter'
ORDER BY tv_genres.name ASC;

