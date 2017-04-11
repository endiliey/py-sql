SELECT director, title, stars
FROM Movie
INNER JOIN Rating USING(mID)
WHERE director is not NULL
GROUP BY director
ORDER BY stars DESC
