-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
SELECT DISTINCT name FROM tv_genres g 
WHERE g.id NOT IN (SELECT genre_id FROM tv_show_genres sg LEFT JOIN tv_shows s ON s.id = sg.show_id WHERE s.title = 'Dexter') 
ORDER BY g.name ASC; 