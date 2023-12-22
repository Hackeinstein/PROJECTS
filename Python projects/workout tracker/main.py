APP_ID = "a761b087"
API_KEY = "042c0cf70df57569f8794ea16b1e0e62"
BEARER_TOKEN="Bearer steintks2023"

import requests
import datetime as dt

nutri_query = input("Tell me which excerises you did: ")

nutri_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutri_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

nutri_params = {
    "query": nutri_query
}

nutri_response = requests.post(url=nutri_url, json=nutri_params, headers=nutri_headers)
nutri_data = nutri_response.json()

# add data to sheets
date = dt.datetime.now().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%H:%M:%S")

sheety_url = "https://api.sheety.co/b4ea4ccf4b1db3a09ad367f5248decfc/copyOfMyWorkouts/workouts"

for exercise in nutri_data["exercises"]:
    sheety_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise['name'],
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        },
    }
    sheety_header = {
        "Content-Type": "application/json",
        "Authorization": BEARER_TOKEN
    }
    sheety_response = requests.post(url=sheety_url, json=sheety_params, headers=sheety_header)
