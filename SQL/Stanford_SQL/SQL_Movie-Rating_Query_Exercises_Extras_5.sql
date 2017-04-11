SELECT distinct A.name, B.name
FROM (Movie
INNER JOIN Rating USING(mID)
INNER JOIN Reviewer R1 USING(rID)) A
INNER JOIN (Movie
INNER JOIN RATING USING(mID)
INNER JOIN Reviewer R2 USING(rID)) B
    ON A.title = B.title AND A.name < B.name
