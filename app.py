import requests
import datetime as dt
import os

"""
# Project 29: Workout Tracking

## Author
- **Name**: Pranjal Sarnaik
- **Date Created**: 17 Jan 2025

## Description:
This project leverages the **Nutritionix API** and **Sheety API** to track your workouts. Users can enter their 
workout details in natural language (e.g., "Ran 3 miles"), and the program:
1. Uses the **Nutritionix API** to understand the exercise and calculate additional details like duration and calories burned.
2. Updates the results, including exercise details, date, and time, into a Google Sheet via the **Sheety API**.

Note: All sensitive information, such as app IDs, API keys, and other credentials, has been removed from this 
documentation to ensure security.

## How to Use:
1. Enter your workout description (e.g., "Cycled for 30 minutes" or "Did 10 push-ups") when prompted.
2. The program will calculate necessary details and add them to your Google Sheet.

## Level
- **Level**: Intermediate
- **Skills**: API integration, Python programming, JSON parsing, HTTP requests, Google Sheets automation.
- **Domain**: Fitness and Health Tracking

## Features
1. **Nutritionix API Integration**: Automatically interprets workout descriptions and calculates calories burned.
2. **Sheety API Integration**: Seamlessly updates workout details into a Google Sheet.
3. **User Input**: Accepts natural language input for exercises.
4. **Dynamic Data**: Automatically includes the current date and time in the Google Sheet.
5. **Organized Codebase**: Includes folders for experiments and alternative methods to solve the problem.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/pranjalco/workout-tracking-using-google-sheets.git
   ```

2. Navigate to the project directory:
   ```bash
   cd workout-tracking-using-google-sheets
   ```

## Running the Program
1. Ensure Python 3.9 or later is installed on your system.
2. To run the program:
   - **Using PyCharm**: Open the project in PyCharm and run `app.py`.
   - **Using Terminal/Command Prompt**: Navigate to the project folder and execute:
     ```bash
     python app.py
     ```
   - **By Double-Clicking**: You can double-click `app.py` to run it directly, provided Python is set up 
   to execute `.py` files on your system.
3. If the console window closes immediately, run the program from the terminal/command prompt or IDE to see the output.

## File Structure
```
workout-tracking/
|
├── app.py                 # Main script to run the program
├── experiments/           # Temporary files or practice scripts
├── other_methods/         # Other methods to solve the problem
├── requirements.txt       # Dependencies for the project
├── README.md              # Project overview and instructions
└── .env                   # Environment variables (excluded from Git)
```

---
**Created by Pranjal Sarnaik**  
*© 2025. All rights reserved.*
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
