-- Check if the user exists
SET @user_exists = (SELECT COUNT(*) FROM mysql.user WHERE user = 'user_0d_1');

-- If the user does not exist, create the user and grant privileges
IF @user_exists = 0 THEN
    CREATE USER 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';
    GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%' WITH GRANT OPTION;
    FLUSH PRIVILEGES;
END IF;

