

import requests
import datetime
import os

api_key = 'c956dd8583b035bae14262f603c4a392'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.datetime.now().strftime("%d %b %y | %I:%M:%S %p")

print("-------------------------------------------------------------------------------------------------------")
print("Weather Starts For - {} || {}".format(location.upper(),date_time))
print("-------------------------------------------------------------------------------------------------------")

print("Current Temperature is: {:.2f} deg C".format(temp_city))
print("Current Weather Description: ",weather_desc)
print("Current Humidity: ",hmdt, '%')
print("Current Wind Speed: ",wind_spd,'kmph')

