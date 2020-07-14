-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
SELECT DISTINCT title 
FROM tv_shows s WHERE s.id NOT IN (SELECT show_id FROM tv_show_genres sg INNER JOIN tv_genres g ON g.id = sg.genre_id WHERE g.name = 'Comedy') 
ORDER BY title ASC; 