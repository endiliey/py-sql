SELECT title, MAX(stars)
FROM Reviewer
INNER JOIN Rating
ON Reviewer.rID = Rating.rID
INNER JOIN Movie
ON Rating.mID = Movie.mID
GROUP BY title
ORDER BY title