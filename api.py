from fastapi import FastAPI , HTTPException , Depends
from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm
from pydantic import BaseModel
from connection import cursor , connection , mariadb
import jwt
from datetime import datetime , timedelta , timezone , date
import bcrypt
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

class Emploeey(BaseModel):
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


SECRET_KEY = "SoltanMahdi:1379"
ALGORITHEM = "HS256"
token_check = OAuth2PasswordBearer(tokenUrl="enter/auth")

def create_token(data : dict):
    data["exp"] = datetime.now(timezone.utc) + timedelta(minutes = 30)
    token = jwt.encode(data , SECRET_KEY , algorithm=ALGORITHEM)
    return token

def verify_token(token : str):
    try:
        data = jwt.decode(token , SECRET_KEY , algorithms=[ALGORITHEM])
        return data
    except:
        raise HTTPException(status_code=401 , detail="Invalid OR expierd token")

app = FastAPI()

@app.post("/enter/auth")
def enter_user(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password

    query = "SELECT username FROM users WHERE username = %s"
    value = [username]
    cursor.execute(query , value)
    result = cursor.fetchone()
    
    if result is not None:
        query = "SELECT pass_hash FROM users WHERE username = %s"
        value = [username]
        cursor.execute(query , value)
        pass_hash1 = cursor.fetchone()[0]

        query2 = "SELECT employee_id FROM users WHERE username = %s"
        value2 = [username]
        cursor.execute(query2 , value2)
        employee_id = cursor.fetchone()

        query3 = "SELECT role_id FROM employees WHERE id = %s"
        value3 = [employee_id[0]]
        cursor.execute(query3 , value3)
        
        role_id = cursor.fetchone()

        res = bcrypt.checkpw(password.encode() , pass_hash1.encode())
        
        if res:
            token = create_token({"username" : username , "role_id" : role_id[0]})
            return {"Massage" : f"Welcome {username}" , "access_token" : token , "token_type": "bearer"}
        
        else:
            raise HTTPException(status_code=401 , detail="Wrong password")
    else:
        raise HTTPException(status_code=401 , detail="Wrong username")

@app.post("/user/enrollment")
def enrollment_user(user_data : EnrollmentData):
    employee_id = user_data.employee_id
    username = user_data.username
    password = user_data.password

    query3 = "SELECT employee_id FROM users WHERE employee_id = %s"
    value3 = [employee_id]
    cursor.execute(query3 , value3)
    ress = cursor.fetchone()

    if ress is not None :
        raise HTTPException(status_code=400 , detail="The emploeey_id you choos is already exists")
        
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
    connection.commit()

    return {"Massage" : f"Welcome to The Samaneh Karmandan {username}"}

@app.post("/Making/emploeey")
def making_emploeeys(* , token : str = Depends(token_check) , emploeey_data : Emploeey):
    name = emploeey_data.name
    familyname = emploeey_data.familyname
    email_address = emploeey_data.email_address
    mobile = emploeey_data.mobile
    hire_date = emploeey_data.hire_date
    role_id = emploeey_data.role_id
    positionn_id = emploeey_data.positionn_id
    situation_id = emploeey_data.situation_id
    department_id = emploeey_data.department_id
    manager_id = emploeey_data.manager_id
    personnel_code = emploeey_data.personnel_code

    data = verify_token(token)
    if data["role_id"] != 1:
        raise HTTPException(status_code=403 , detail= "sorry.You dont have acsses for doing this")
    else:
        query = """INSERT INTO employees (name , familyname , email_address ,
                   mobile , hire_date , role_id , positionn_id , situation_id,
                   department_id , manager_id , personnel_code)
                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = [name , familyname , email_address ,mobile , hire_date ,
                  role_id , positionn_id , situation_id, department_id , 
                  manager_id , personnel_code]

        cursor.execute(query , values)
        connection.commit()

        return {"Massage" : "The emploeey aded succsesfuly"}