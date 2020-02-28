import requests
import time
import datetime
from geopy.geocoders import Nominatim 

geolocator = Nominatim(user_agent='Marco')

def get_flights(fly_from, fly_to, 
                date_from, date_to, 
                roundtrip = False,
                return_from=None, return_to=None, 
                adults=1, children=0, infants=0,
                budget=1500, currency='USD',
                people=0, 
                max_duration=50, 
                radius=50, radius_format= 'km',):
    '''
    Gets possible flights given search parameters.
    Args:
        fly_from (String or double tuple) - City from where you are leaving (string - city name, double tuple - lat,lon of city)
        fly_to (String or double tuple) - City you will be flying into 
        date_from (String) - Minimum departure date, formatted as DD/MM/YYYY
        date_to (String) - Maximum departure date, formatted as DD/MM/YYYY
        budget (Int) - Itinerary budget (in inputted currencies)
        
        Optional Args:
        return_from (String) - Minimum return date (i.e, the earliest you would like to return to fly_from)
        return_to (String) - Maximum return date (i.e., the latest you would like to return to fly_from)
        radius (String) - Distance of airport from city. Default 50. Default is suggested.
    Return:
        final_data - List of dictionaries, each entry contains particular flight data
        Each entry of the form:
            {'price':price of the flight
             'Itinerary' - Holds all the legs of the flight and associated information
             'total_duration': Total flight duration in hours.
             'link': Link to kiwi.com listing.
            }
    
    '''
    outbound = geolocator.geocode(fly_from)
    out_lat = outbound.latitude
    out_lon = outbound.longitude

    inbound = geolocator.geocode(fly_to)
    in_lat = inbound.latitude
    in_lon = inbound.longitude

    fly_from = str(round(out_lat,2)) + '-' + str(round(out_lon,2)) + '-' + str(radius) + radius_format
    fly_to = str(round(in_lat,2)) + '-' + str(round(in_lon,2)) + '-' + str(radius) + radius_format

    #adults=adults, children=children, infants=infants, return_from=return_from,return_to=return_to
    url = 'https://api.skypicker.com/flights?fly_from={}&fly_to={}&date_from={}&date_to={}&curr={}&sort={}&partner=picky&v=3'.format(\
          fly_from, fly_to, date_from, date_to, 'USD', 'price')

    flight_response = requests.get(url)
    flight_resp_dict = flight_response.json()
    flight_data = flight_resp_dict['data']
    filt_flight_data = [x for x in flight_data if float(x['price'])<= budget and float(x['fly_duration'].split('h')[0]) <= max_duration]
    print(filt_flight_data)
    final_data = [None]*len(filt_flight_data)
    for i in range(0,len(final_data)):
        final_data[i] = {'price':filt_flight_data[i]['price'], 
                        'Itinerary':[(
                                    (leg['cityFrom'],leg['cityTo']),
                                    (leg['flyFrom'],leg['flyTo']),
                                     leg['operating_carrier']+leg['operating_flight_no'],
                                     leg
                                     )
                                    for leg in filt_flight_data[i]['route']],
                        "total_duration":float(filt_flight_data[i]['fly_duration'].split('h')[0]),
                        "link":filt_flight_data[i]['deep_link'],
                        'start_dest':(filt_flight_data[i]['cityFrom'],filt_flight_data[i]['flyFrom'],filt_flight_data[i]['countryFrom']['name']),
                        'end_dest':(filt_flight_data[i]['cityTo'],filt_flight_data[i]['flyTo'],filt_flight_data[i]['countryTo']['name'])
                        }

    return final_data





