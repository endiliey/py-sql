insert into Rating  ( rID, mID, stars, ratingDate )
select Reviewer.rID , Movie.mID, 5, null 
from Movie
left outer join Reviewer
where Reviewer.name='James Cameron'
