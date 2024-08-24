import requests
from datetime import datetime 

USERNAME = "hariom123"
TOKEN = "hariom5266"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
# hjkh34h3jk4hj34h3jh4 anglenas token and usernmae is anglena
user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":'yes',
}

# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint  = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":"graph1",
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai",
}

headers = {
    "X-USER-TOKEN":TOKEN
}

response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

# Add a pixel to the graph

pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

# today = datetime.now()
today = datetime(year=2024, day=23, month=8)

pixel_data = {
    "date": today.strftime("%Y%m%d"),  
    "quantity": "129.74",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

# print(response.status_code)  # Check the status code
# print(response.text)          

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity":"12"
}

# response=requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response=requests.delete(url=delete_endpoint,headers=headers)
print(response.text)



