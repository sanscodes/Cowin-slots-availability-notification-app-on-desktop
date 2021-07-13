import time
import requests
from plyer import notification
from playsound import playsound

dist = 457

date = '13-07-2021'
URL = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={dist}&date={date}'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 '
                  'Safari/537.36'}


def findAvailability():
    counter = 0
    result = requests.get(URL, headers=header)
    response_json = result.json()
    data = response_json["sessions"]
    for each in data:
        if (each["available_capacity"] > 0) & (18 <= each["min_age_limit"] <= 45):
            counter += 1
            print(f'Name of the place : {each["name"]}')
            print(f'PIN code : {each["pincode"]}')
            print(f'Vaccine name : {each["vaccine"]}')
            print(f'No of Doses available :{each["available_capacity_dose2"]}')
            playsound('ding-sound.mp3')
            notification.notify(
                title="Hey!! slots for dose 2 are  available",
                message="Book now!",
                app_icon="Iconshow-Medical-Injection.ico",
                timeout=10
            )
            time.sleep(900)
            return True
    if counter == 0:
        print("No Available Slots")
        return False


while not findAvailability():
    time.sleep(5)
    findAvailability()
    notification.notify(
        title="Hey!! slots for dose 2 are not available",
        message="Have patience till you get notified",
        app_icon="Iconshow-Medical-Injection.ico",
        timeout=60
    )
    time.sleep(900)
