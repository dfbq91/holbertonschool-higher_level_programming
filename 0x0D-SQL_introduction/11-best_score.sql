-- Lists records of a table showing two columns filtered with an order
SELECT `score`, `name` FROM `second_table`
WHERE `score` >= 10 ORDER BY `score` DESC;