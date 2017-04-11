SELECT distinct name
FROM Reviewer
INNER JOIN Rating USING(rID)
INNER JOIN Movie USING(mID)
WHERE title = 'Gone with the Wind'
