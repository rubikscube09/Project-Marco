'''
Code for getting weather related data
'''

import requests
import time
import datetime
# install geopy by 'pip install geopy'
from geopy.geocoders import Nominatim

# convert city name into latitude and longitude
city = 'Chicago' # sample city
geolocator = Nominatim(user_agent='marco')
location = geolocator.geocode(city)
lat = location.latitude
lat = str(lat)
lon = location.longitude
lon = str(lon)

# historical weather data using Darksky API
API_key0 = '9b36894c88b4232f066c1fec6b2e3511'
# 1000 free calls per day

request_url0 = 'https://api.darksky.net/forecast/' + API_key0 + '/'
# make sure the lat lon have the correct signs
request_url0 += lat + ',' + lon
# the date we want historical data from, in UNIX, sample date 1/12/2011
date = int(datetime.datetime.strptime('1/23/2001', "%m/%d/%Y").timestamp())
request_url0 += ',' + str(date)

weather_response0 = requests.get(request_url0)
weather_json0 = weather_response0.json()
# the data of interest is in 
weather_json0['daily']['data']

# 16 day forecast weather data using Weatherbit API
API_Key1 = '01a7197ed8294958ab4c7c6662cbb01c'
# 500 calls per day

request_url1 = 'https://api.weatherbit.io/v2.0/forecast/daily?key=' + API_Key1
request_url1 += '&lat=' + lat + '&lon=' + lon

weather_response1 = requests.get(request_url1)
weather_json1 = weather_response1.json()
# check documentation for where to get data