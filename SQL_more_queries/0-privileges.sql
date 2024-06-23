-- Create a script named `0-privileges.sql` that lists all privileges of `user_0d_1` and `user_0d_2`

-- Ensure you are using the MySQL server
USE mysql;

-- Show grants for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show grants for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';

