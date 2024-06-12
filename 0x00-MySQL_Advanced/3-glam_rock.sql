--  Calculate the lifespan of glam rock bands.
SELECT band_name AS band_name, IFNULL(split, 2022) - IFNULL(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
