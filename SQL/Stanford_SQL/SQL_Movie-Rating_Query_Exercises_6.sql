--SELECT name, title
--FROM Movie
--INNER JOIN Rating R1 USING(mId)
--INNER JOIN Rating R2 USING(rId)
--INNER JOIN Reviewer USING(rId)
--WHERE R1.mId = R2.mId AND R1.ratingDate < R2.ratingDate AND R1.stars < R2.stars;

SELECT Name, Title
FROM Movie
INNER JOIN Rating R1
ON Movie.mID = R1.mID
INNER JOIN Rating R2
ON Movie.mID = R2.mID
INNER JOIN Reviewer
ON R1.rID = Reviewer.RID AND R2.rID = Reviewer.RID
WHERE R1.stars > R2.stars AND R1.ratingDate > R2.ratingDate