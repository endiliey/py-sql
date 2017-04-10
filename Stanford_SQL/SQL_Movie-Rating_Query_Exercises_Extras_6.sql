SELECT name, title, MIN(stars)
FROM Movie
INNER JOIN Rating USING(mID)
INNER JOIN Reviewer USING(rID)
GROUP BY name, title
HAVING MIN(stars) in (SELECT MIN(stars) FROM Rating)
