# Project 29: Workout Tracking

## Author
- **Name**: Pranjal Sarnaik
- **Date Created**: 17 Jan 2025

## Description:
This project leverages the **Nutritionix API** and **Sheety API** to track your workouts. Users can enter their workout details in natural language (e.g., "Ran 3 miles"), and the program:
1. Uses the **Nutritionix API** to understand the exercise and calculate additional details like duration and calories burned.
2. Updates the results, including exercise details, date, and time, into a Google Sheet via the **Sheety API**.

Note: All sensitive information, such as app IDs, API keys, and other credentials, has been removed from this documentation to ensure security.

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
   - **By Double-Clicking**: You can double-click `app.py` to run it directly, provided Python is set up to execute `.py` files on your system.
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

