import requests
from datetime import datetime
import smtplib

MY_LAT = 30.332184 # Your latitude
MY_LONG = -81.655647 # Your longitude
# MY_LAT = -27.332184# Your latitude
# MY_LONG = -65.655647 # Your longitude

def iss_is_close(my_lat, my_long, iss_lat, iss_long):
    print(f"{my_lat-iss_lat} {my_long-iss_long} {iss_lat} {iss_long}")
    if ((my_lat - iss_lat < 5.0) and (my_lat - iss_lat > -5.0 )) and ((my_long - iss_long < 5.0) and (my_long - iss_long > -5.0)):
        return True
    else:
        return False

def is_day(hour, sunrise_hour, sunset_hour):
    #print(f"{hour} {sunrise_hour} {sunset_hour}")
    if sunset_hour == 0:
        sunset_hour = 24
    if (hour > sunrise_hour) and (hour < sunset_hour):
        return True
    else:
        return False
    

def send_email():
    myEmail = "email@email.com"
    myPassword = "<<key>>"

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=myEmail, password=myPassword)
        connection.sendmail(
            from_addr=myEmail, 
            to_addrs = myEmail, 
            msg="Subject:Look Up\n\nThe ISS is Overhead!"
        )


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.utcnow().hour





#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

if (is_day(time_now, sunrise, sunset)) and (iss_is_close(MY_LAT,MY_LONG,iss_latitude, iss_longitude)):
    send_email()


