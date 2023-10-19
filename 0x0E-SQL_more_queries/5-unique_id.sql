-- This creates unique_id table on current database
CREATE TABLE IF NOT EXISTS unique_id (
id INT DEFAULT 1 UNIQUE,
name VARCHAR(256)
);
