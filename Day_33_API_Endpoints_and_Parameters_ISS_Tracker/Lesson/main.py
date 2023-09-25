import requests
from datetime import datetime


# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# #print(response)
# response.raise_for_status()
# data = response.json()
# #print(data)
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (latitude,longitude)
# print(iss_position)

MY_LAT = 30.332184
MY_LNG = -81.655647
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise)
print(sunrise.split("T")[1].split(':')[0])

time_now = datetime.utcnow()
print(time_now)