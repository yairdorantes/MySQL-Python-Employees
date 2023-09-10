import mysql.connector


def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1",
    )
    cursor = connection.cursor()
    cursor.execute("USE Employees;")
    return cursor, connection
