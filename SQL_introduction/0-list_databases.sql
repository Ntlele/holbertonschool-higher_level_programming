import mysql.connector  # -- Import the mysql.connector module to interact with MySQL
from mysql.connector import Error  # -- Import the Error class for handling exceptions

def list_databases():
    try:
        -- Establish the connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost', 
            user='root',
            password='password'
        )

        -- Check if the connection was successful
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SHOW DATABASES")

            print("List of databases:")
            for db in cursor:
                print(db[0])

    except Error as e:
        print(f"Error: {e}")

    finally:
        -- Ensure that the cursor and connection are closed properly
        if connection.is_connected():
            cursor.close()
            connection.close()

