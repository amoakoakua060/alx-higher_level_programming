-- This lists the number of records with the same score in second_table of current database
SELECT `score`, COUNT(*) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `number`;
