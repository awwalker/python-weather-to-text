#!/usr/bin/env python3
import sys
import forecastio
import requests
import json
from datetime import datetime

#get api
api_key = "3906d93478a5bec947b1c43b1f896fa8"

#local time
current_time = datetime.utcnow()
print(current_time.date())
#retrieve location
def get_location():
    send_url = 'http://freegeoip.net/json/'
    req = requests.get(send_url)
    j = json.loads(req.text)
    lat = j['latitude']
    lon = j['longitude']
    return lat, lon

coords = get_location()
lat = coords[0]
lon = coords[1]

#initiate
forecast = forecastio.load_forecast(api_key, lat, lon, time = current_time)

byHour = forecast.hourly()

for data in byHour.data:
    if data.time.utcnow().date() == current_time.date():
        print(data.time, data.icon, data.temperature)
