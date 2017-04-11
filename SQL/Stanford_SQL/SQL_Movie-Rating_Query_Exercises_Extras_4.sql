SELECT title
FROM Movie
WHERE title NOT IN (SELECT title FROM Movie
INNER JOIN Rating USING(mID)
INNER JOIN Reviewer USING(rID)
WHERE name = 'Chris Jackson')
