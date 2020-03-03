-- Displays the top 3 MAX temperatures (Fahrenheit)
-- by city ordered by temperature (descending)
SELECT state, MAX(value) AS max_temp
FROM temperatures GROUP BY state
ORDER BY state;