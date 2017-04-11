SELECT first.name, first.grade, second.name, second.grade
FROM Likes, Highschooler first, Highschooler second
WHERE Likes.ID1 = first.ID AND Likes.ID2 = second.ID
AND ID2 NOT IN(SELECT ID1 FROM Likes)
