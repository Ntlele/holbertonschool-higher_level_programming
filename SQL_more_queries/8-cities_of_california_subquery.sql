-- Select all cities from the cities table that belong to the state of California
-- Get the state_id for California from the states table using a subquery
-- Results are sorted in ascending order by cities.id

SELECT * FROM cities
WHERE state_id = (
	    SELECT id FROM states
	    WHERE name = 'California'
)
ORDER BY id ASC;
