import requests
import os

#Update with lat/long coordinates
MY_LAT = 0
MY_LONG = 0

api_key = os.environ.get("OPENWEATHERMAP_API_KEY")
url = "http://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "units": "imperial",
    "cnt": 12,
    "appid": api_key,
}

response = requests.get(url=url, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour in weather_data["list"]:
    #Weather IDs less than 700 mean there will be precipitation (ie snow, rain, etc)
    if hour["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella!")
else:
    print("You can leave the umbrella at home.")


