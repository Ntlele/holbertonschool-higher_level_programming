-- Create table 'id_not_null' if it doesn't exist
CREATE TABLE IF NOT EXISTS id_not_null (
	    id INT DEFAULT 1,    -- Integer column 'id' with default value 1
	    name VARCHAR(256)    -- Variable character column 'name' with max length 256
	);

