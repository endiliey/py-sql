SELECT DISTINCT CITY
FROM STATION
WHERE SUBSTR(CITY, -1, 1) NOT IN ('a', 'e', 'i', 'o', 'u')
AND SUBSTR(CITY, 1, 1) NOT IN ('a', 'e', 'i', 'o', 'u')