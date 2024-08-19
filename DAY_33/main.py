# response=requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)

# 1xx : Hold On
# 2xx: Here You Go
# 3xx: Go Away
# 4xx: You screwed Up

# print(response.status_code)

# if response.status_code == 404:
#     raise Exception("That resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorixed to access this data")


# response.raise_for_status()

# data = response.json()
# # print(data)
# longitude = response.json()['iss_position']['longitude']
# latitude = response.json()['iss_position']['latitude']

# iss_position = (longitude,latitude)
# print(iss_position)

# https://sunrise-sunset.org/api --> Sunrise & Sunset

import requests
import datetime

MY_LAT = 22.468480
MY_LNG = 70.057290
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    'formatted':0,
}

# Corrected URL without the period at the end
response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
# print(data)
sunrise=data['results']['sunrise'].split('T')[1].split(':')[0]
sunset=data['results']['sunset'].split('T')[1].split(':')[0]

print(sunrise)
print(sunset)

time_now = datetime.datetime.now()
print(time_now.hour)







