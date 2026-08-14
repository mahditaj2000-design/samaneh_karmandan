from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from connection import cursor , connection , mariadb
import jwt
from datetime import datetime , timedelta , timezone

SECRET_KEY = "SoltanMahdi:1379"
ALGORITHEM = "HS256"

def create_token(data : dict):
    token["exp"] = datetime.now() + timedelta(minutes = 30)
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
        pass_hash1 = cursor.fetchone()

        if pass_hash1 is not None and pass_hash == pass_hash1[0]:
            token = create_token({"username" : username})
            return {"Massage" : "user enter succesfuly" , "token" : token}
        
        else:
            raise HTTPException(status_code=401 , detail="Wrong password")
    else:
        raise HTTPException(status_code=401 , detail="Wrong username")
    