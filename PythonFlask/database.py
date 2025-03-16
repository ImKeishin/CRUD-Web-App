import mysql.connector

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="cristi12",
            database="cinema"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None