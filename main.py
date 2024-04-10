import random

import pyodbc

server = 'DESKTOP-2DB5AH1\\MSSQLSERVER01'
database = 'PKO_MP'
username = 'login'
password = 'pass'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                      SERVER=' + server + ';\
                      DATABASE=' + database + ';\
                      UID=' + username + ';\
                      PWD=' + password)

cursor = cnxn.cursor()



# List of names
names = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Charles", "Thomas",
    "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan", "Jessica", "Sarah", "Karen"]

surnames = [
    "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
    "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson"
]

for i in range(1, 1000):
    UserID = i
    LastName = random.choice(surnames)
    FirstName = random.choice(names)
    query = f"INSERT INTO Users (UserID, LastName, FirstName) VALUES ({UserID}, '{LastName}', '{FirstName}')"
    cursor.execute(query)
    cursor.commit()

query = "SELECT * FROM Users"
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)

# query = "DELETE FROM Users WHERE 1=1"
# cursor.execute(query)
# cursor.commit()


cursor.close()
