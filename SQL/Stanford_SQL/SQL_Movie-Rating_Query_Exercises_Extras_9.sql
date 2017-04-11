SELECT title, director
FROM Movie
WHERE director IN (SELECT director FROM Movie GROUP BY director HAVING COUNT(title) > 1)
ORDER BY director, title
