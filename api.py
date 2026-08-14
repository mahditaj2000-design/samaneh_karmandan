from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from connection import cursor , connection , mariadb
import jwt
from datetime import datetime , timedelta , timezone
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

SECRET_KEY = "SoltanMahdi:1379"
ALGORITHEM = "HS256"

def create_token(data : dict):
    data["exp"] = datetime.now(timezone.utc) + timedelta(minutes = 30)
    token = jwt.encode(data , SECRET_KEY , algorithm=ALGORITHEM)
    return token

app = FastAPI()

@app.post("/enter/auth")
def enter_user(username : str , pass_hash : str):

    query = "SELECT username FROM users WHERE username = %s"
    value = [username]
    cursor.execute(query , value)
    result = cursor.fetchone()
    
    if result is not None:
        query = "SELECT pass_hash FROM users WHERE username = %s"
        value = [username]
        cursor.execute(query , value)
        pass_hash1 = cursor.fetchone()[0]

        res = bcrypt.checkpw(pass_hash.encode() , pass_hash1.encode())
        
        if res:
            token = create_token({"username" : username})
            return {"Massage" : "user enter succesfuly" , "token" : token}
        
        else:
            raise HTTPException(status_code=401 , detail="Wrong password")
    else:
        raise HTTPException(status_code=401 , detail="Wrong username")

@app.post("/user/enrollment")
def enrollment_user(employee_id : str , username : str , password : str):
    
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

    return {"Massage" : "Welcome to The Samaneh Karmandan"}
    