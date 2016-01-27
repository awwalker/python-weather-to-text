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

look into icons.

"""

#get apis
twil_api_account = "ACf73ced0c380899d61668998ee7f91c98"
twil_api_token = "5d593fb432c3365c32634f2b55773b5a"

twil_client = TwilioRestClient(twil_api_account, twil_api_token)
fore_api_key = "3906d93478a5bec947b1c43b1f896fa8"

#local time adjusted with timezone
current_time = datetime.now(pytz.timezone("US/Eastern"))

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

#initiate based on current time
forecast = forecastio.load_forecast(fore_api_key, lat, lon, current_time)

byHour = forecast.hourly()

message = ""
for data in byHour.data:
    #only really want data for the day today and the hours after the current hour
    if data.time.date() == date and data.time.time() >= current_time.time():
        #just write the time, forecast and temperature for each hour
        message += data.time.strftime("%I:%M%p") + " -- {0} at {1} degrees".format(data.summary, data.temperature) + "\n"

to_me = twil_client.messages.create(
to = "+14086465533",
from_ = "+14087522765",
body = message)
