import requests
from datetime import datetime

API_ID="06b73ad0"
API_KEY1="8361fa02f38799af80d8dc41608fb0e5"
API_KEY2="8b312a58c1f60e9f4c3c47f2006109b1"
NUTRITIONX_API="https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_API="https://api.sheety.co/177a757c11f1af958fe07b046b5c8544/workoutTracking/myworkout"
SHEETY_Token="Shubham@1"

HEADER={
    "x-app-id":API_ID,
    "x-app-key":API_KEY1
}

PARAMETERES={
    "query":input("Enter your workout: "),
    "gender":input("Enter your gender: "),
    "weight_kg":input("Enter your weight: "),
    "age":input("Enter your age: "),
    "height_cm":input("Enter your height in cm: ")
}

response= requests.post(url=NUTRITIONX_API,json=PARAMETERES,headers=HEADER)
print(response.json())
date=datetime.now().date().strftime("%d/%m/%y")
time=datetime.time(datetime.now()).strftime("%H:%M:%S")
exercise=response.json()["exercises"][0]["user_input"]
duration=response.json()["exercises"][0]["duration_min"]
calories=response.json()["exercises"][0]["nf_calories"]

RECORD={
    "myworkout":{
        "date":date,
        "time":time,
        "exercise":exercise,
        "duration":f"{duration}min",
        "calories":calories,
    }
    
}
SHEETY_HEADER={
    "Authorization": "Bearer Shubham@1"
}
respose=requests.post(url=SHEETY_API,json=RECORD,headers=SHEETY_HEADER)