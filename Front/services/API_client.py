import requests

BASE_URL = "http://127.0.0.1:8000"

ACCSESS_TOKEN = None

def login(username , password):
    url = f"{BASE_URL}/enter/auth"

    global ACCSESS_TOKEN

    form_data = {"username":username,
                 "password":password}

    response = requests.post(url , data = form_data)

    if response.status_code == 200:
        result = response.json()
        ACCSESS_TOKEN = result["access_token"]
        return result
    else:
        return {

            "status_code":response.status_code,
            "detail":response.json().get("detail")
        }

def get_auth_header():                   #برای برگرداندن توکن در هدر که بعدی ای پی ای های محافظت شده بتونن به جای هر بار فراخوانی توکن بیان از این فانکشن استفاده کنن

    return {
        "Authorization":f"Bearer {ACCSESS_TOKEN}"
    }

def get_me():
    url = f"{BASE_URL}/get_me"

    response = requests.get(url , headers=get_auth_header())

    result = response.json()

    if response.status_code == 200:

        return result

    else:

        return {

            "status_code":response.status_code,
            "detail":response.json().get("detail")
        }

def edit_my_prof(new_data):
    url = f"{BASE_URL}/edit_my_prof"

    response = requests.patch(url , headers=get_auth_header() , json=new_data)

    if response.status_code == 200:
        return response.json()
    else:
        return {
            "status_code": response.status_code,
            "detail": response.json().get("detail")
        }

def change_password(password_data):
    url = f"{BASE_URL}/change_password"

    response = requests.patch(url , headers=get_auth_header() , json=password_data)

    if response.status_code == 200:
        return response.json()
    else:
        return {
            "status_code": response.status_code,
            "detail": response.json().get("detail")
        }