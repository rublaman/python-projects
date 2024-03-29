import requests
import os
from datetime import datetime

# NUTRITIONIX
APP_ID = os.environ.get("APP_ID", "APP ID it doesn't exist")
API_KEY = os.environ.get("API_KEY", "API_KEY it doesn't exist")

url = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

user_input = input("Which exercise you did? ")

data = {
    "query": user_input
}

response_nutritionix = requests.post(url, headers=headers, json=data)
if response_nutritionix.status_code == 200:
    response_nutritionix = response_nutritionix.json()
    print(response_nutritionix)
else:
    print(f"Error in the request. Status code: {response_nutritionix.status_code}")
    print(response_nutritionix.text)

# SHEETY
SHEETY_API_URL = "https://api.sheety.co/----------/workoutTracking/workouts"

headers = {
  'Authorization': f'Basic ---------'
}

today = datetime.now()
today_str = today.strftime('%d/%m/%Y')
time_str = today.strftime("%H:%M:%S")
name = response_nutritionix['exercises'][0]['name'].title()
duration = response_nutritionix['exercises'][0]['duration_min']
calories = response_nutritionix['exercises'][0]['nf_calories']

data = {
  "workout": {
    "date": today_str,
    "time": time_str,
    "exercise": name,
    "duration": duration,
    "calories": calories
  }
}

response = requests.post(SHEETY_API_URL, json=data, headers=headers)
