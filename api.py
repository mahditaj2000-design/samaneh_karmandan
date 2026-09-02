from fastapi import FastAPI , HTTPException , Depends
from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm
from pydantic import BaseModel , Field
from connection import pool , mariadb
import jwt
from jwt import InvalidTokenError, ExpiredSignatureError
from datetime import datetime , timedelta , timezone , date
import bcrypt
from dotenv import load_dotenv
import os
from typing import Optional

common_passwords = [
    "password", "123456", "123456789", "12345678", "12345", "1234567",
    "qwerty", "abc123", "111111", "123123", "admin", "letmein",
    "welcome", "monkey", "login", "princess", "qwertyuiop", "solo",
    "passw0rd", "starwars", "dragon", "master", "hello", "freedom",
    "whatever", "qazwsx", "trustno1", "654321", "1qaz2wsx", "iloveyou",
    "1q2w3e4r", "000000", "zaq1zaq1", "football", "baseball", "shadow",
    "michael", "jennifer", "jordan", "superman", "harley", "hunter",
    "ranger", "buster", "soccer", "tigger", "charlie", "andrew",
    "matthew", "computer", "michelle", "jessica", "pepper", "1111",
    "zxcvbn", "555555", "11111111", "131313", "sunshine", "chicken",
    "corvette", "bigdog", "cheese", "hockey", "yankees", "bulldog",
    "amanda", "ashley", "hannah", "joshua", "george", "asshole",
    "asdf", "asdfgh", "asdfghjkl", "121212", "222222", "aaaaaa",
    "adobe123", "photoshop", "1234", "azerty", "000000", "gizmodo",
    "test", "guest", "root", "toor", "changeme", "temp", "temp123",
    "default", "administrator", "letmein123", "passw0rd1", "p@ssw0rd",
    "q1w2e3r4", "1qazxsw2", "zzzzzz", "qwerty123", "iloveyou1"
]

class EnrollmentData(BaseModel):
    employee_id : int
    username : str
    password : str


class search_data(BaseModel):
    name : Optional[str] = None
    familyname : Optional[str] = None
    email_address : Optional[str] = None
    mobile : Optional[str] = None
    hire_date : Optional[date] = None
    role_id : Optional[int] = None
    positionn_id : Optional[int] = None
    situation_id : Optional[int] = None
    department_id : Optional[int] = None
    manager_id : Optional[int] = None
    personnel_code : Optional[str] = None

class employee(BaseModel):
    name : str
    familyname : str
    email_address : str = None
    mobile : str
    hire_date : date
    role_id : int
    positionn_id : int
    situation_id : int
    department_id : int
    manager_id : int = None
    personnel_code : str

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY is missing")
ALGORITHEM = "HS256"
token_man = OAuth2PasswordBearer(tokenUrl="/enter/auth")

def search_data_fillter(name:str=None,
familyname:str=None,
email_address:str=None,
mobile:str=None,
hire_date:date=None,
role_id:int=None,
positionn_id:int=None,
situation_id:int=None,
department_id:int=None,
manager_id:int=None,
personnel_code:str=None):

    return search_data(name=name,
    familyname=familyname,
    email_address=email_address,
    mobile=mobile,
    hire_date=hire_date,
    role_id=role_id,
    positionn_id=positionn_id,
    situation_id=situation_id,
    department_id=department_id,
    manager_id=manager_id,
    personnel_code=personnel_code)

def false_enter(username: str, conn, cursor):

    query = """
    INSERT INTO login_attempts
    (username, attempt_time, success)
    VALUES (%s, NOW(), FALSE)
    """

    cursor.execute(query, [username])
    conn.commit()

def true_enter(username:str , conn , cursor):

    query = """
    INSERT INTO login_attempts
    (username, attempt_time, success)
    VALUES (%s, NOW(), TRUE)
    """

    cursor.execute(query, [username])
    conn.commit()


def get_conn():
    conn = pool.get_connection()
    cursor = conn.cursor()
    try:
        yield conn , cursor
    finally:
        cursor.close()
        conn.close()

def create_token(data : dict):
    data["exp"] = datetime.now(timezone.utc) + timedelta(minutes = 30)
    token = jwt.encode(data , SECRET_KEY , algorithm=ALGORITHEM)
    return token

def verify_token(token : str):
    try:
        data = jwt.decode(token , SECRET_KEY , algorithms=[ALGORITHEM])
        return data
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Expired TOKEN")
    except InvalidTokenError:
        raise HTTPException(status_code=401 , detail="Invalid TOKEN")

def check_manager(token = Depends(token_man)):
    data = verify_token(token)  
    if data["role_id"] != 1:
        raise HTTPException(status_code=403 , detail= "sorry.You dont have acsses for doing this")
    return data

def token_check(token=Depends(token_man)):
    data = verify_token(token)
    return data

app = FastAPI()

@app.post("/enter/auth")
def enter_user(Form_data : OAuth2PasswordRequestForm = Depends() , db=Depends(get_conn)):

    conn , cursor = db

    username = Form_data.username
    password = Form_data.password

    query = """
    SELECT COUNT(*)
    FROM login_attempts
    WHERE username = %s
    AND success = FALSE
    AND attempt_time > NOW() - INTERVAL 10 MINUTE
    """

    cursor.execute(query, [username])
    failed_count = cursor.fetchone()[0]

    if failed_count>=4:
        raise HTTPException(status_code=429 , detail="""تعداد تلاش های ناموفق شما بیش از 4 بار بود.
          لطفا بعدا تلاش کنید""")


    query = """SELECT users.pass_hash , employees.role_id
    FROM users
    JOIN employees ON employees.id = users.employee_id
    WHERE users.username = %s"""
    value = [username]

    cursor.execute(query , value)
    res = cursor.fetchone()

    if res is None:
            false_enter(username , conn , cursor)
            raise HTTPException(status_code=401 , detail="Wronge username or password")
    
    else:
        result = bcrypt.checkpw(password.encode() , res[0].encode())
        if result is False:
            false_enter(username , conn , cursor)
            raise HTTPException(status_code=401 , detail="Wronge username or password")
        else:
            if res[1] < 1 or res[1] > 2 :
                raise HTTPException(status_code=401 , detail="Wronge username or password")
            else:
                true_enter(username , conn , cursor)
                token = create_token({"username":username , "role_id":res[1]})
                return {
                       "Massage":"Wellcome to samaneh karmandan","access_token":token , "token_type":"bearer"
                    }

@app.post("/user/enrollment")
def enrollment_user(user_data : EnrollmentData , db=Depends(get_conn) , data=Depends(check_manager)):

    conn , cursor = db

    employee_id = user_data.employee_id
    username = user_data.username
    password = user_data.password

    query3 = "SELECT employee_id FROM users WHERE employee_id = %s"
    value3 = [employee_id]
    cursor.execute(query3 , value3)
    ress = cursor.fetchone()

    if ress is not None :
        raise HTTPException(status_code=400 , detail="The employee_id you choos is already exists")
    if username == "" or password == "" :
        raise HTTPException(status_code=400 , detail="Wrong username or password")
    if password in common_passwords or len(password)<8 :
        raise HTTPException(status_code=400 , detail="weak password")

    query2 = "SELECT username FROM users WHERE username = %s"
    value2 = [username]

    cursor.execute(query2 , value2)
    result = cursor.fetchone()

    if result is not None:
        raise HTTPException(status_code=400 , detail="The username you choos is already exists")

    pass_hash = bcrypt.hashpw(password.encode() , bcrypt.gensalt()).decode()
        
    query = "INSERT INTO users(employee_id , username , pass_hash) VALUES (%s , %s , %s)"
    values = [employee_id , username , pass_hash]

    cursor.execute(query , values)
    conn.commit()

    return {"Massage" : f"Welcome to The Samaneh Karmandan {username}"}

@app.post("/Making/employee")
def making_employees(employee_data : employee,
                     db=Depends(get_conn),
                     data=Depends(check_manager)):

    conn , cursor = db

    name = employee_data.name
    familyname = employee_data.familyname
    email_address = employee_data.email_address
    mobile = employee_data.mobile
    hire_date = employee_data.hire_date
    role_id = employee_data.role_id
    positionn_id = employee_data.positionn_id
    situation_id = employee_data.situation_id
    department_id = employee_data.department_id
    manager_id = employee_data.manager_id
    personnel_code = employee_data.personnel_code

    query = """INSERT INTO employees (name , familyname , email_address ,
            mobile , hire_date , role_id , positionn_id , situation_id,
            department_id , manager_id , personnel_code)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    values = [name , familyname , email_address ,mobile , hire_date ,
            role_id , positionn_id , situation_id, department_id , 
            manager_id , personnel_code]
    cursor.execute(query , values)
    conn.commit()
    return {"Massage" : "The employee aded succsesfuly"}

@app.get("/get_employees")
def get_employees(db=Depends(get_conn) , data=Depends(check_manager)):
    conn , cursor = db
    query = """SELECT * FROM employees"""
    cursor.execute(query)
    res = cursor.fetchall()

    return {"Massage":"عملیات با موفقیت انجام شد" , "result":res}

@app.get("/get_me")
def get_me(db=Depends(get_conn) , data=Depends(token_check)):
    conn , cursor = db

    query = """SELECT employees.*
    FROM users
    JOIN employees ON users.employee_id = employees.id
    WHERE users.username = %s"""
    value = [data["username"]]

    cursor.execute(query, value)
    result = cursor.fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="Employee record not found")

    return {"Massage":"عملیات با موفقیت انجام شد" , "res":result}

@app.get("/search_employee")
def search(search_data=Depends(search_data_fillter) , db=Depends(get_conn) , data=Depends(token_check)):
    conn , cursor = db

    condition = []
    value = []

    quary = """SELECT * FROM employees WHERE """

    if search_data.name:
        condition.append("name = %s")
        value.append(search_data.name)

    if search_data.familyname:
        condition.append("familyname = %s")
        value.append(search_data.familyname)

    if search_data.email_address:
        condition.append("email_address = %s")
        value.append(search_data.email_address)

    if search_data.mobile:
        condition.append("mobile = %s")
        value.append(search_data.mobile)

    if search_data.hire_date:
        condition.append("hire_date = %s")
        value.append(search_data.hire_date)

    if search_data.role_id:
        condition.append("role_id = %s")
        value.append(search_data.role_id)

    if search_data.positionn_id:
        condition.append("positionn_id = %s")
        value.append(search_data.positionn_id)

    if search_data.situation_id:
        condition.append("situation_id = %s")
        value.append(search_data.situation_id)

    if search_data.department_id:
        condition.append("department_id = %s")
        value.append(search_data.department_id)

    if search_data.manager_id:
        condition.append("manager_id = %s")
        value.append(search_data.manager_id)

    if search_data.personnel_code:
        condition.append("personnel_code = %s")
        value.append(search_data.personnel_code)

    if condition:

        quary+= " AND ".join(condition)

        cursor.execute(quary , value)
        res = cursor.fetchall()
        
        return {"Massage":f"{res}"}

    else:
        return{"Massage":"لطفا یک فیلتر انتخاب کنید"}

@app.delete("/delete_employee")
def delete_employee(personnel_code:str,db=Depends(get_conn) , data=Depends(check_manager)):
    conn , cursor = db

    value = [personnel_code]
    cursor.execute(("""SELECT * FROM employees WHERE personnel_code = %s""") , value)
    res = cursor.fetchall() #اصلا یه همچین کارمندی هست؟
    cursor.execute(("""SELECT id FROM employees WHERE personnel_code = %s""") , value)
    res2 = cursor.fetchone() #اگر یه همچین کارمندی باشه حالا id اون رو داریم

    if res:

        quary = """SELECT * FROM users WHERE employee_id = %s"""
        value1 = res2

        cursor.execute(quary , value1)
        res3 = cursor.fetchall()

    else:
        return {"Massage":"کارمند مورد نظر یافت نشد"}
    
    if res3:

        quary = """DELETE FROM users WHERE employee_id = %s"""
        value2 = res2
        cursor.execute(quary , value2)
        conn.commit()
        
        quary = """DELETE FROM employees WHERE personnel_code = %s"""
        value3 = [personnel_code]
        cursor.execute(quary , value3)
        conn.commit()

        return {"Massage":"کارمند مورد نظر با موفقیت از لیست کارمندان حذف شد"}

    if res and not res3:

        quary = """DELETE FROM employees WHERE personnel_code = %s"""
        value4 = [personnel_code]
        cursor.execute(quary , value4)
        conn.commit()

        return {"Massage":"کارمند مورد نظر با موفقیت حذف شد"}
