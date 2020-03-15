'''
Code for getting weather related data
'''

import requests
import datetime
from geopy.geocoders import Nominatim

def weather(city, date_in_str):
    '''
    Getting the weather information of a specific city at one day.

    Input:
    city: string
    date_in_str: string in the format 'yyyy-mm-dd'
    '''
    # convert city name into latitude and longitude
    #city = input('Enter City Name: ') 
    geolocator = Nominatim(user_agent='marco')
    location = geolocator.geocode(city)
    lat = location.latitude
    lat = str(lat)
    lon = location.longitude
    lon = str(lon)

    #date_in_str = input('Enter date of interest(yyyy-mm-dd): ')
    date_in = datetime.datetime.strptime(date_in_str, "%Y-%m-%d")
    today = datetime.datetime.today()
    # calculate difference between input date and today's date
    day_diff = date_in - today
    day_diff = day_diff.days

    if day_diff < 0 or day_diff > 16:
        # if the input date is in the past or the input date is beyond
        # the 16 day forecast range, use darksky api for historical weather

        API_key0 = '9b36894c88b4232f066c1fec6b2e3511'
        # 1000 free calls per day

        request_url0 = 'https://api.darksky.net/forecast/' + API_key0 + '/'
        # make sure the lat lon have the correct signs
        request_url0 += lat + ',' + lon
        # if the input day is beyond the 16 day forecast range, dial the year
        # of the input one year back to get an estimate
        if day_diff > 16:
            date_in = date_in.replace(year = date_in.year - 1)
        # the date we want historical data from, in UNIX
        date = int(date_in.timestamp())
        request_url0 += ',' + str(date)

        weather_response0 = requests.get(request_url0)
        weather_json0 = weather_response0.json()
        data0 = weather_json0['daily']['data'][0]
        # apparent Temperature High and Low
        app_temp_h = data0['apparentTemperatureHigh']
        app_temp_l = data0['apparentTemperatureLow']
        # rainfall probability
        prob_precip = data0['precipProbability']
        av_temp = (app_temp_h + app_temp_l) / 2
        return (av_temp, prob_precip)

    else:
        # 16 day forecast weather data using Weatherbit API
        API_Key1 = '01a7197ed8294958ab4c7c6662cbb01c'
        # 500 calls per day

        request_url1 = 'https://api.weatherbit.io/v2.0/forecast/daily?key=' + API_Key1
        request_url1 += '&lat=' + lat + '&lon=' + lon

        weather_response1 = requests.get(request_url1)
        weather_json1 = weather_response1.json()
        data1 = weather_json1['data']

        for day in data1:
            if day['datetime'] == date_in_str:
                # apparent temps
                max_t = day["app_max_temp"]
                min_t = day["app_min_temp"]
                # chance of rain
                precip = day['precip']
            
        av_temp = (max_t + min_t) / 2
        return (av_temp, precip)