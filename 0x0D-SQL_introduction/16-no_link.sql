-- This lists all records of second_table with name not empty in current database
SELECT `score`, `name` FROM `second_table` WHERE `name` != '' ORDER BY `score` DESC;
