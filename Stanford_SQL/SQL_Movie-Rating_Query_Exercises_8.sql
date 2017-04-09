SELECT title, (MAX(stars) - MIN(stars)) as diff
FROM Reviewer
INNER JOIN Rating
ON Reviewer.rID = Rating.rID
INNER JOIN Movie
ON Rating.mID = Movie.mID
GROUP BY title
HAVING MAX(stars) != MIN(stars)
ORDER BY diff DESC, title