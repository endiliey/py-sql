SELECT name, title, stars
FROM Reviewer
INNER JOIN Rating USING(rID)
INNER JOIN Movie USING(mID)
WHERE name = director
