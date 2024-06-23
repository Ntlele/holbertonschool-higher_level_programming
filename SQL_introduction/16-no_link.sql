-- List all records from second_table with non-empty name values, ordered by descending score
SELECT score, name
FROM `second_table`
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
