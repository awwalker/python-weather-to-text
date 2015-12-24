#!/usr/bin/env python3
import sys
import pytz
import forecastio
import requests
import json
from datetime import datetime

#get api
api_key = "YOUR KEY"

#local time
current_time = datetime.now(pytz.timezone("US/Eastern"))
date = current_time.now().date()
print(current_time)
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
    #only really want data for the day today and the hours after the current hour
    if data.time.date() == date and data.time.time() >= current_time.now().time():
