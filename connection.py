import mariadb

pool = None

try:
    pool = mariadb.ConnectionPool(
        pool_name="my_pool",
        pool_size=6,
        host = "localhost",
        user = "root",
        password = "",
        port = 3307,
        database = "employee_management"
    )
    print("connected")

except mariadb.Error as error:
  print(error)