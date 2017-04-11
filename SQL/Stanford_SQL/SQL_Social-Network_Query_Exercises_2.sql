SELECT first.name, first.grade, second.name, second.grade
FROM Likes
INNER JOIN Highschooler as first
    ON first.ID = Likes.ID1
INNER JOIN Highschooler as second
    ON second.ID = Likes.ID2
WHERE first.grade - second.grade >= 2
