import requests
import datetime as dt
import os

"""
p29: workout tracking
date: 17 Jan 2025
"""

GENDER = "male"
WEIGHT_KG = 48
HEIGHT_CM = 175
AGE = 28

APP_ID = "app_id"
API_KEY = "api_key"

USER_INPUT = input("Please enter exercise description: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_info = {
    "query": USER_INPUT,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

host_domain = "https://trackapi.nutritionix.com"
exercise_endpoint = f"{host_domain}/v2/natural/exercise"
sheety_endpoint = "sheety_endpoint"

response = requests.post(url=exercise_endpoint, headers=headers, json=exercise_info)
exercise_data = response.json()

exercise = exercise_data['exercises'][0]["user_input"]
duration = exercise_data['exercises'][0]["duration_min"]
calories = exercise_data['exercises'][0]["nf_calories"]

today = dt.datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_time = today.strftime("%H:%M:%S")

sheety_data = {
    "workout": {"date": today_date,
                "time": today_time,
                "exercise": exercise,
                "duration": duration,
                "calories": calories,
                }
}

bearer_token = "bearer_token"
auth_headers = {
    "Authorization": f"Bearer {bearer_token}"
}

sheety_response = requests.post(url=sheety_endpoint, json=sheety_data, headers=auth_headers)
print(sheety_response.json())
