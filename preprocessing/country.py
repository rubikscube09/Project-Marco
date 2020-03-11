#Get country from ity name geopy's AEPI.
from geopy.geocoders import Nominatim
import re

CORRECTIONS_DIC={'United States of America': 'United States',
'Jamaika': 'Jamaica'}

geolocator = Nominatim(user_agent='marco')

def get_country(city):
    '''
    A function to get (cleaned) country from city name.
    '''
    try:
        location = geolocator.geocode(city, language='en-US')
        country = location.address.split(',')[-1].strip()
        if country in CORRECTIONS_DIC:
            country=CORRECTIONS_DIC[country]
        return(country)
    except:
        print("error for "+city)
        return("ERR")
