-- Create database 'hbtn_0d_usa' if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database 'hbtn_0d_usa'
USE hbtn_0d_usa;

-- Create table 'states' if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
	    id INT AUTO_INCREMENT PRIMARY KEY,  -- Integer column 'id' with auto-increment, unique, not null, and primary key constraints
	    name VARCHAR(256) NOT NULL          -- Variable character column 'name' with max length 256 and not null constraint
	);

