'''
Skeleton code for getting weather related data
'''

import requests

# historical weather data using Darksky API
API_key0 = '9b36894c88b4232f066c1fec6b2e3511'
# 1000 free calls per day

request_url0 = 'https://api.darksky.net/forecast/' + API_key0 + '/'
lat = # get latitude of city A with some other function
lon = # get longiture of city B with some other function
# make sure the lat lon have the correct signs
request_url0 += lat + ',' + lon
date = # the date we want historical data from, in UNIX
request_url0 += ',' + date

weather_response0 = requests.get(request_url0)
weather_json0 = weather_response.json()
# the data of interest is in 
weather_json0['daily']['data']

# 16 day forecast weather data using Weatherbit API
API_Key1 = '01a7197ed8294958ab4c7c6662cbb01c'
# 500 calls per day

request_url1 = 'https://api.weatherbit.io/v2.0/forecast/daily?key=' + API_key1
requset_url1 += '&lat=' + lat + '&lon=' + lon

weather_response1 = requests.get(request_url1)
weather_json1 = weather_response1.json()
# check documentation for where to get data

