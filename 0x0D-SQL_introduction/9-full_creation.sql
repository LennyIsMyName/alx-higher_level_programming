-- Create another table and insert multiple rows

CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name varchar(256),
	score INT
	)

INSERT INTO second_table (d, name, score)
VALUES (1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
