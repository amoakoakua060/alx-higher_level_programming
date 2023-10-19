-- This lists all shows contained in tv_shows that have at least one genre linked
-- if a show doesn’t have a genre, display NULL
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT OUTER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
