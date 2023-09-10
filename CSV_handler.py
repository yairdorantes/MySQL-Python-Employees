import pandas as pd
from MainDB import add_employee
from DBConnection import create_connection

cursor, connection = create_connection()
# Read the CSV file into a DataFrame
df = pd.read_csv("employees.csv")
for index, row in df.iterrows():
    employee = (row[0], row[1], row[2], row[3], row[4], row[5])
    # print(employee)
    # employee = ("1", "2", "3", "4", "5", "6")
    add_employee(employee, cursor)


connection.commit()
cursor.close()
connection.close()
