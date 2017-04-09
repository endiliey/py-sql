SELECT distinct year
FROM Movie
INNER JOIN Rating
    ON Movie.MID = Rating.MID
WHERE Rating.stars = 4 or Rating.Stars = 5
ORDER BY year