#Habit Tracker

import datetime
import requests

today = datetime.datetime.now()

pixela_endpoint ="https://pixe.la/v1/users"
user_params = {
    "token":"d9vo1df6dn3hkndv",
    "username":"sairaj",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"

}
graph_endpoint = f"{pixela_endpoint}/sairaj/graphs"
graph_params={
    "id":"graph1234",
    "name":"S Traker",
    "unit":"count",
    "type":"int",
    "color":"ajisai"
}
http_headers ={
    "X-USER-TOKEN":"d9vo1df6dn3hkndv"
}
pixel_entry_endpoint = "https://pixe.la/v1/users/sairaj/graphs/graph1234"
pixel_entry= {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("What is the quantity:")
}
response = requests.post(url=pixel_entry_endpoint,json=pixel_entry,headers=http_headers)
print(response.text)


# Creating Graph
# response =requests.post(url=graph_endpoint,json=graph_params,headers=http_headers)
# print(response.text)

# Creating User
# response =requests.post(url=pixela_endpoint,json=parameters)
# print(response.text)
