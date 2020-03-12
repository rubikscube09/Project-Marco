import requests
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
                radius=50, radius_format= 'km'):
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

    #Long and Lat of inputted location
    outbound = geolocator.geocode(fly_from)
    out_lat = outbound.latitude
    out_lon = outbound.longitude

    inbound = geolocator.geocode(fly_to)
    in_lat = inbound.latitude
    in_lon = inbound.longitude

    #Convert to format lat-long-radius
    fly_from = str(round(out_lat,2)) + '-' + str(round(out_lon,2)) + '-' + str(radius) + radius_format
    fly_to = str(round(in_lat,2)) + '-' + str(round(in_lon,2)) + '-' + str(radius) + radius_format

    url = 'https://api.skypicker.com/flights?fly_from={}&fly_to={}&date_from={}&date_to={}&curr={}&sort={}&partner=picky&v=3'.format(\
          fly_from, fly_to, date_from, date_to, 'USD', 'price')

    #Case for roundtrip flights
    if roundtrip:
        assert return_from != None and return_to != None, 'Please specify locations'
        url += '&return_from={}&return_to={}'.format(return_from, return_to)
    if adults != 1:
        url += '&adults={}'.format(adults)
    if children != 0:
        url += '&children={}'.format(children)
    if infants != 0:
        url += '&infants={}'.format(infants)

    flight_response = requests.get(url)
    flight_resp_dict = flight_response.json()
    try:
        flight_data = flight_resp_dict['data']
        # Condition that flight is not too long and not too expensive
        filt_flight_data = [x for x in flight_data if float(x['price'])<= budget and float(x['fly_duration'].split('h')[0]) <= max_duration]
        
        final_data = [None]*len(filt_flight_data)
        #Final output containing total price, duration, destinations, and legs of journey w/ associated flight numbers..
        for i in range(0,len(final_data)):
            final_data[i] = {'price':filt_flight_data[i]['price'], 
                            'Itinerary':[((leg['cityFrom'],leg['cityTo']),
                                        (leg['flyFrom'],leg['flyTo']),
                                         leg['airline']+str(leg['flight_no']))
                                        for leg in filt_flight_data[i]['route']],
                            "total_duration":float(filt_flight_data[i]['fly_duration'].split('h')[0]),
                            "link":filt_flight_data[i]['deep_link'],
                            'start_dest':(filt_flight_data[i]['cityFrom'],filt_flight_data[i]['flyFrom'],filt_flight_data[i]['countryFrom']['name']),
                            'end_dest':(filt_flight_data[i]['cityTo'],filt_flight_data[i]['flyTo'],filt_flight_data[i]['countryTo']['name'])
                            }

        return sorted(final_data, key=lambda data: data['price'])
    except:
        print(date_from, date_to)
        return 'Flight data unavailable'





