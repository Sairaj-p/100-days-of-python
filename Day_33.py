#API ISS Notifier

import requests
from datetime import datetime
import smtplib
import time


def iss_overhead():
    my_pos ={
        "lat":73.069908,
        "lng":73.069908
        }
    response =requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()["iss_position"]
    longi =float(data["longitude"])
    lati = float(data["latitude"])
    if my_pos["lat"]-5 <= lati <= my_pos["lat"]+5 and my_pos["lng"]-5<=longi<=my_pos["lng"+5]:
        return True
    else:
        return False

def is_dark():
    my_time = datetime.now()
    my_time_hr = my_time.hour
    response = requests.get(url="https://api.sunrise-sunset.org/json",params=my_pos)
    response.raise_for_status()
    time_data = response.json()
    sunrise = int(time_data["results"]["sunrise"].split("T")[0].split(":")[0])
    sunset =  int(time_data["results"]["sunset"].split("T")[0].split(":")[0])
    if my_time_hr<sunrise or my_time_hr>sunset:
        return True
    else:
        return False
while True:
    time.sleep(300)
    if iss_overhead() and is_dark:
        email ="example@gmail.com"
        password ="12345678"
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(email,password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg="Subject:Alert\n\nThe International Space Station is above you!"
        )
