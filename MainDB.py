from DBConnection import create_connection

cursor, connection = create_connection()

cursor.execute("CREATE DATABASE IF NOT EXISTS Employees")

cursor.execute("USE Employees")
# Table employees
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Employees (
        id_employee INT AUTO_INCREMENT PRIMARY KEY,
        name CHAR(50),
        lastname CHAR(50),
        email CHAR(50),
        phone CHAR(50),
        city CHAR(50),
        country CHAR(50)
    )
"""
)
# Table attendance
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Attendance
    (
        id_attendance INT AUTO_INCREMENT PRIMARY KEY,
        id_employee INT NOT NULL,
        date_attendance DATE NOT NULL,
        entrance TIME NOT NULL,
        departure TIME NOT NULL
    )
    """
)
# Table payments
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Payments
    (
        id_payment INT AUTO_INCREMENT PRIMARY KEY,
        employee INT NOT NULL,
        payment_account INT NOT NULL,
        date_payment DATE NOT NULL,
        payment_amount FLOAT NOT NULL,
        FOREIGN KEY(employee) REFERENCES Employees(id_employee) ON DELETE CASCADE
    )
    """
)

# create sotore procedure
cursor.execute(
    """
CREATE PROCEDURE IF NOT EXISTS sp_add_employee(
    IN i_name VARCHAR(50),
    IN i_lastname VARCHAR(50),
    IN i_email VARCHAR(50),
    IN i_phone VARCHAR(50),
    IN i_city VARCHAR(50),
    IN i_country VARCHAR(50)
)
BEGIN
    INSERT INTO Employees (name, lastname, email, phone, city, country)
    VALUES (i_name, i_lastname, i_email, i_phone, i_city, i_country);
END;
    """
)


# add employees
def add_employee(employee, cursor):
    insert_query = """
    CALL sp_add_employee(%s, %s, %s, %s, %s, %s);
    """
    cursor.execute(insert_query, employee)


connection.commit()
connection.close()
