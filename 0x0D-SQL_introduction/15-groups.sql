-- Lists the # of records with the same score in a table of a database
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score DESC;