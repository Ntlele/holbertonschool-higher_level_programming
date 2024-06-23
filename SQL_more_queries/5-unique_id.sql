-- Create table 'unique_id' if it doesn't exist
CREATE TABLE IF NOT EXISTS unique_id (
	    id INT DEFAULT 1 UNIQUE,  -- Integer column 'id' with default value 1 and unique constraint
	    name VARCHAR(256)         -- Variable character column 'name' with max length 256
	);
