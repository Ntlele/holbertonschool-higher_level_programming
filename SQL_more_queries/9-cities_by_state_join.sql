-- Select cities.id, cities.name, and states.name for all cities in the hbtn_0d_usa database
-- Join the cities and states tables on the state_id and id columns to get the state name for each city
-- Sort the results in ascending order by cities.id

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
