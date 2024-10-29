import requests
from datetime import datetime
import smtplib
import time

# Email authentication 
my_email = "Add your email"
password = "Add the app password"
smtp = "Your smtp"
recipient = "Reciever's email"

MY_LAT = "Your latitude"
MY_LONG = "Your longitude"

# To check if the ISS is flying near our location
def is_iss_near():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        return True

# To check is it is night time currently at our location
def is_it_night():
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

    if time_now <= sunrise or sunset <= time_now: 
        return True

# To send email notification
def send_notif():
    if is_iss_near() and is_it_night():
        with smtplib.SMTP(smtp, port=587) as connection:
            connection.starttls()
            connection.login(user = my_email, password = password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=recipient, 
                msg= "Subject:Look up!\n\nLook up, the ISS is here.")
                
# To run this code every minute
while True:
    send_notif()
    time.sleep(60)

