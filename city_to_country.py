'''
Standalone code that converts a city into a country
When you run this code, a prompt will pop up asking you the name of the city.
Need to install geopy on your machine
'''

from geopy.geocoders import Nominatim
import re

# convert city name into latitude and longitude
city = input('Enter City Name: ') 
geolocator = Nominatim(user_agent='marco')
location = geolocator.geocode(city, language='en-US')
country = location.address.split(',')[-1].strip()
print(country)