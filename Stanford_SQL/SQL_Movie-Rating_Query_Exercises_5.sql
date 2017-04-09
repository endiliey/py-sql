SELECT Reviewer.Name, Movie.Title, Rating.Stars, Rating.ratingDate
FROM Reviewer
INNER JOIN Rating
ON Reviewer.rID = Rating.rID
INNER JOIN Movie
ON Rating.mID = Movie.mID
ORDER BY Reviewer.name, Movie.Title, Rating.Stars