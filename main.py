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

query = "SELECT * FROM Users"
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
