#Get country from ity name geopy's AEPI.
from geopy.geocoders import Nominatim
import re

CORRECTIONS_DIC={'United States of America': 'United States',
'Jamaika': 'Jamaica'}

geolocator = Nominatim(user_agent='marco')

def get_country(city):
    '''

    Matches city to country using the geopy api. 

    Input: string, city
    Output: string, no_country if none of the countries matches the city name.
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
