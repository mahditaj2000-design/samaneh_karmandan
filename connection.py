import mariadb

connection = None

try:
    connection = mariadb.connect(
        host = "localhost",
        user = "root",
        password = "",
        port = 3307,
        database="employee_management"
    )
    cursor = connection.cursor()
    print("connected")
    
except mariadb.Error as error:
    print(error)
