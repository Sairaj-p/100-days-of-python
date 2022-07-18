# Cheap Flight finder 

import requests
import datetime

sheety_read ="https://api.sheety.co/41c79c766b37bfd3ee3619ab9b419c8a/day39/sheet1"


# def get_des_code(city):
#     code_endpoint ="https://tequila-api.kiwi.com/locations/query"
#     header ={"apikey":"wA1-z2Ba6ZCYINM5G-oudOhE2hpCqLeM"}
#     query_ ={"term":city,"location_types":"city"}
#     response = requests.get(url=code_endpoint,headers=header,params=query_)
#     data = response.json()
#     return data["locations"][0]["code"]


# response = requests.get(url=sheety_read)
# Data_sheet = response.json()["sheet1"]
# for i in range(0,len(Data_sheet)):
#     Data_sheet[i]["iataCode"] = get_des_code(Data_sheet[i]["city"])
#     new_data = {
#                 "sheet1": {
#                     "iataCode": get_des_code(Data_sheet[i]["city"])
#                 }
#             }
#     Sheety_put = f"https://api.sheety.co/41c79c766b37bfd3ee3619ab9b419c8a/day39/sheet1/{i+2}"
#     response = requests.put(url=Sheety_put,json=new_data)
#     response.raise_for_status()

def flight_price(code):
    Flight_search ="https://tequila-api.kiwi.com/v2/search"
    header={
        "apikey":"wA1-z2Ba6ZCYINM5G-oudOhE2hpCqLeM"
    }
    params={
        "fly_from":"LON",
        "fly_to":code,
        "date_from": (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d/%m/%Y"),
        "data_to":(datetime.datetime.now() + datetime.timedelta(days=180)).strftime("%d/%m/%Y")
    }
    response = requests.get(url=Flight_search,headers=header,params=params)
    response.raise_for_status()
    data = response.json()["data"][0]
    price = data["price"]
    return price

response = requests.get(url=sheety_read)
Data = response.json()["sheet1"]
for i in range(0,len(Data)):
    city = Data[i]["city"]
    price = flight_price(Data[i]["iataCode"])
    if Data[i]["lowestPrice"] > price:
        new_data = {
                "sheet1": {
                    "lowestPrice": price
                }
            }
        Sheety_put = f"https://api.sheety.co/41c79c766b37bfd3ee3619ab9b419c8a/day39/sheet1/{i+2}"
        response = requests.put(url=Sheety_put,json=new_data)
        response.raise_for_status()

