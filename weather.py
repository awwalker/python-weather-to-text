#!/usr/bin/env python3
import sys
import pytz
import forecastio
import requests
import json
from datetime import datetime
from twilio.rest import TwilioRestClient

"""
TO DO:

cron job.
test multiline message.
look into icons.
make public.
use.
"""

#get apis
twil_api_account = "Your Account"
twil_api_token = "Your token"

twil_client = TwilioRestClient(twil_api_account, twil_api_token)
fore_api_key = "Your key"

#local time adjusted with timezone
current_time = datetime.now(pytz.timezone("US/Pacific-New"))
#just date
date = current_time.now().date()


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
forecast = forecastio.load_forecast(fore_api_key, lat, lon, time = current_time)

byHour = forecast.hourly()
message = ""
for data in byHour.data:
    #only really want data for the day today and the hours after the current hour
    if data.time.date() == date and data.time.time() >= current_time.now().time():
        message += data.time.strftime("%B %d, %I:%M%p") + " -- {0} at {1} degrees".format(data.summary, data.temperature) + "\n"
        print(message)
to_me = twil_client.messages.create(
to = "+your cell",
from_ = "+your twilio number",
body = "\n" + message)
