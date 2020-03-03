-- Lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT id, name FROM cities
WHERE state_id IN (
    SELECT state_id FROM states
    WHERE NAME = "California"
    ORDER BY state_id
);