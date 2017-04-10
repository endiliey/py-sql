SELECT name, grade
FROM Highschooler
WHERE ID not IN (SELECT ID1 FROM Likes)
AND ID not IN (SELECT ID2 From Likes)
ORDER BY grade, name
