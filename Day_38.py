# Workout Tracker

import requests
from datetime import datetime

Nutritix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutrix_header ={
    "x-app-id":"84687a47",
    "x-app-key":"6b3cde226684fd78a55d122250296781",
    "Content-Type": "application/json"
}
nutrix_params ={
 "query":input("Today's Exercise : "),
 "gender":"male",
 "weight_kg":70,
 "height_cm":168,
 "age":18
}



response = requests.post(url=Nutritix_endpoint,headers=nutrix_header,json=nutrix_params)
try:
    Data = response.json()["exercises"][0]
except:
    print("Invalid Input")
else:  
    activity = Data["name"]
    time_active = Data["duration_min"]
    calories = Data["nf_calories"]
    print(activity,time_active,calories)

    sheety_endpoint ='https://api.sheety.co/41c79c766b37bfd3ee3619ab9b419c8a/workout/sheet1'
    sheet_inputs = {
        "sheet1": {
        "date": datetime.now().strftime("%d/%m/%Y"),
        "time": datetime.now().strftime("%X"),
        "exercise": activity,
        "duration": time_active,
        "calories": calories
        }
        }

    sheet_response = requests.post(url=sheety_endpoint,json=sheet_inputs)
    print(sheet_response.text)
