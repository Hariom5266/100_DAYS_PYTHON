import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 42
HEIGHT_CM = 160
AGE = 16

APP_ID = ""
API_KEY = ""
TOKEN = "="  

exercise_endpoint = ""
sheet_endpoint = ""

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {  # Ensure the root property matches your sheet name
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)
