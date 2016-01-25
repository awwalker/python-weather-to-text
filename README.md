# python-weather-to-text
This Python script is designed to simplify my mornings. As easy as it is to open the weather app on my phone every morning I find it somewhat annoying. I am always having to look at my messages though. So now using this script I can have a text message of the upcoming day's weather sent to me in the morning as I wake up.

I used Twilio and Forecast.io in the script to facilitate the messaging and the grabbing of the weather data. A simple cron job set as root enables the script to be run every morning at 9:00AM.
