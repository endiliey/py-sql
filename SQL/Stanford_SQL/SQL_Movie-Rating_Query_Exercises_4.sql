SELECT name
FROM Reviewer
INNER JOIN Rating
ON Reviewer.rID = Rating.rID
WHERE Rating.ratingDate is NULL