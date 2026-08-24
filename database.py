from connection import pool,mariadb

connection = None
cursor = None

connection = pool.get_connection()
cursor = connection.cursor()
try:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS roles (
    role_name VARCHAR(100) NOT NULL UNIQUE,
    id INT AUTO_INCREMENT PRIMARY KEY)
    ENGINE=InnoDB""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS situation (
    situation_name VARCHAR(60) NOT NULL,
    id INT AUTO_INCREMENT PRIMARY KEY)
    ENGINE=InnoDB""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS positionn (
    positionn_name VARCHAR(70),
    id INT PRIMARY KEY AUTO_INCREMENT)
    ENGINE=InnoDB""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS department (
    department_name VARCHAR(100),
    id INT PRIMARY KEY AUTO_INCREMENT)
    ENGINE=InnoDB""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        familyname VARCHAR(100) NOT NULL,
        email_address VARCHAR(100) UNIQUE,
        mobile VARCHAR(11) NOT NULL UNIQUE,
        hire_date DATE NOT NULL,
        role_id INT NOT NULL,
        positionn_id INT NOT NULL,
        situation_id INT NOT NULL,
        department_id INT NOT NULL,
        manager_id INT,
        personnel_code VARCHAR(20) NOT NULL UNIQUE,
        
        FOREIGN KEY (role_id) REFERENCES roles(id),
        FOREIGN KEY (positionn_id) REFERENCES positionn(id),
        FOREIGN KEY (department_id) REFERENCES department(id),
        FOREIGN KEY (situation_id) REFERENCES situation(id),
        FOREIGN KEY (manager_id) REFERENCES employees(id)
        )
    ENGINE=InnoDB""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id  INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT NOT NULL,
    last_visit DATETIME,
    username VARCHAR(50) UNIQUE NOT NULL,
    pass_hash VARCHAR(200) NOT NULL,
    
    FOREIGN KEY (employee_id) REFERENCES employees(id)
    )

    ENGINE=InnoDB""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS login_attempts(
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    attempt_time DATETIME NOT NULL,
    success BOOLEAN NOT NULL)""")

    connection.commit()
    print("opperation succied")
except mariadb.Error as e:
    print(e)

finally:
    if connection:
        connection.close()