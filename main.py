import random
import names
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


def add_random_users_to_db(number_of_iteration):
    for i in range(1, number_of_iteration + 1):
        LastName = names.get_last_name()
        FirstName = names.get_first_name()
        query = (f"INSERT INTO Users (LastName, FirstName) VALUES ('{LastName}','{FirstName}')")
        cursor.execute(query)
    cursor.commit()


def show_all_users():
    query = "SELECT * FROM Users"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def delete_all_users():
    query = "DELETE FROM Users WHERE 1=1"
    cursor.execute(query)
    cursor.commit()
    # query = "ALTER TABLE Users AUTO_INCREMENT = 1;"
    # cursor.execute(query)
    # cursor.commit()


while True:
    print(f"Hello Mr Mateusz. What do you want to do with this app?\n")
    print(f"a Show all users\n")
    print(f"b Delete all users\n")
    print(f"c Add users\n")
    print(f"d Exit app\n")
    # print("\n")

    choice = input("Type letter: ")
    print("\n")
    if choice == 'a':
        show_all_users()
    if choice == 'b':
        delete_all_users()
    if choice == 'c':
        how_many = int(input("How many: "))
        add_random_users_to_db(how_many)
        print("\n")
    if choice == 'd':
        break
