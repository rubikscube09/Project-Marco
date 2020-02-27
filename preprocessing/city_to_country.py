#Get country from ity name geopy's AEPI.
from geopy.geocoders import Nominatim
import re

CORRECTIONS_DIC={'United States of America': 'United States',
'Jamaika': 'Jamaica'}

def get_country(city):
    '''
    A function to get (cleaned) country from city name.
    '''
    geolocator = Nominatim(user_agent='marco')
    location = geolocator.geocode(city, language='en-US')
    country = location.address.split(',')[-1].strip()
    if country in CORRECTIONS_DIC:
        country=CORRECTIONS_DIC[country]
    return(country)