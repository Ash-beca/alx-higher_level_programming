-- Lists all shows and genres linked to the show from the
-- database hbtn_0d_tvshows.
-- Records are ordered by ascending show title and genre name.
SELECT tv_shows.title AS title
      FROM tv_shows
      LEFT JOIN tv_show_genres 
      ON tv_genres.id = s.show_id
      LEFT JOIN tv_genres
      ON tv.genre_id = name.id
      ORDER BY title, name;
