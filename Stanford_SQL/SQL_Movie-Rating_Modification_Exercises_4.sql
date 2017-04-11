delete from rating
where mID in (select mID from movie where year < 1970 or year > 2000)
and stars < 4
