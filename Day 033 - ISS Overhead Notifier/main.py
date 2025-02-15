import smtplib
import requests
from datetime import datetime
import time

MY_EMAIL = """My email"""
MY_PASSWORD = """My email's app password"""

MY_LAT = """MY actual Latitude"""
MY_LONG = """My actual Longitude"""

def is_near_ISS():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    #Your position is within +5 or -5 degrees of the ISS position.
    return (MY_LAT-5 <= iss_latitude <= MY_LAT+5) and (MY_LONG-5 <= iss_longitude <= MY_LONG+5)

def is_dark():
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

    time_now = datetime.now().hour

    return time_now >= sunset or time_now <= sunrise

while True:
    if is_near_ISS() and is_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look up! ISS is above YOU!\n\nLook up! ISS is above YOU!"
            )
    time.sleep(60)

