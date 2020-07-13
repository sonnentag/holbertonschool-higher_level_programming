-- create another table if it doesn't exist
-- and add multiple values this time
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(255), score INT);
INSERT INTO second_table (id, name, score) VALUES (1, "John", 10), (2, "Alex", 3), (3, "Bob", 14), (4, "George", 8); 
