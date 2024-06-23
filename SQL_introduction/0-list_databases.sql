import mysql.connector
from mysql.connector import Error
"""
This module checks for the MYSQL databases
"""

def list_databases():
    try:
        # Establish the connection to MySQL
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SHOW DATABASES")

            print("List of databases:")
            for db in cursor:
                print(db[0])

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

