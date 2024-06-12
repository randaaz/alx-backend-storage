--  Retrieve the total number of fans for metal bands grouped by origin.
SELECT origin AS origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
