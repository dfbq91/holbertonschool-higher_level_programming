-- Lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT id, name FROM cities -- Columns for the output
WHERE state_id IN ( -- state_id is the foreign key that point to id of states table
    SELECT id FROM states
    WHERE NAME = "California"
    ORDER BY state_id
);