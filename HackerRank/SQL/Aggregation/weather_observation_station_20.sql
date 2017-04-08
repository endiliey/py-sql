SELECT ROUND(S.LAT_N,4) AS median
FROM station S
    WHERE (SELECT COUNT(LAT_N) FROM STATION WHERE LAT_N < S.LAT_N) =
          (SELECT COUNT(LAT_N) FROM STATION WHERE LAT_N > S.LAT_N)