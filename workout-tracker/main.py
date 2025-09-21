import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GENDER = os.environ.get("GENDER")
WEIGHT_KG = os.environ.get("WEIGHT_KG")
HEIGHT_CM = os.environ.get("HEIGHT_CM")
AGE = os.environ.get("AGE")

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
TOKEN = os.environ.get("TOKEN")

today = datetime.now()
time = today.strftime("%X")
date = today.strftime("%d/%m/%Y")

# Nutritionix API
endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
params = {
    "query": input("Tell me which exercise you did?: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
response = requests.post(url=endpoint, json=params, headers=headers)
data = response.json()

# Sheety API
header_sheet = {
    "Authorization": f"Basic {TOKEN}"
}
sheet_endpoint = "https://api.sheety.co/9b30db2c7346994f92963d4310313982/workoutTracking/workouts"

for exercise in data.get("exercises", []):
    sheet_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response_1 = requests.post(url=sheet_endpoint, json=sheet_params, headers=header_sheet)
    print(response_1.text)
