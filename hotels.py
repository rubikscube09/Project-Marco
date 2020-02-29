import requests
from geopy.geocoders import Nominatim 

# Getting Hotels and associated information using the TripAdvisor hotels and location API. 500 calls/day , 1 call/second 
# Might be 250/day because we have to call 2 APIs

def get_location_id(location):

    '''
    Gets the tripadvisor location_id

    Args:
        location (Str): Name of location whose trip advisor id is needed. 
                        location input is usually a city name, but I'm not sure if we need to do longiude and latitude.

    Returns:
        location_id(int): trip advisor location id of the location.
    '''
    url = "https://tripadvisor1.p.rapidapi.com/locations/search"

    querystring = { 'query':location,
                    'location_id' : '1',
                    'limit' : '1',
                    'sort' : 'relevance',
                    'offset' : '0',
                    'lang' : 'en_US',
    }

    headers = {
        'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
        'x-rapidapi-key': "21a93f3e0emsh34914a994184bdep12923cjsnc90566e5ca81"
        }

    response = requests.request('GET',url,headers=headers,params = querystring)
    return response.json()['data'][0]['result_object']['location_id']

def get_hotels(location, 
               num_adults,
               check_in,nights,
               rooms=1,
               currency='USD',
               minprice=0,budget=20000, 
               sort_by ='price',
               order='asc',
               limit=10):
    '''
    Find appropriate hotels in a given location.

    Args(Required)
        location_id (Str): TripAdvisor location_id obtained in get_location call
        num_adults (int): Number of adults needing accomodations
        rooms (int) : Number of rooms booked
    
    Args(Optional)
        check_in (Str): Check in date. Optional but highly suggested for relevance. Format YYYY-MM-DD 
        nights (int): Number of nights to stay.
        sort_by (Str): What to sort the query by 
        minprice (float): Minimum amount (/night) to be spent in given currency. Default Value 0 
        budget (float): Maximum amount (/night) that one would like to spend. Default Value 10000
        amenities 
        limit (int): Number of entries 

    '''
    url = "https://tripadvisor1.p.rapidapi.com/hotels/list"
    location_id = get_location_id(location)
    querystring = { 'location_id' : str(location_id),
                    'adults': str(num_adults),
                    'pricesmax':str(budget),
                    'check_in':check_in,
                    'nights':str(nights),
                    'rooms':str(rooms),
                    'limit':str(limit),
    }

    headers = {
        'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
        'x-rapidapi-key': "21a93f3e0emsh34914a994184bdep12923cjsnc90566e5ca81"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    resp_data = response.json()['data']
    #Sort output by average price (low price + high price/2)
    resp_data_price_sort = sorted(resp_data, key = lambda x: (int(x['price'].split()[0].strip('$')) + int(x['price'].split()[2].strip('$')))/2)
    return [(data['name'],data['price'],(data['latitude'],data['longitude'])) for data in resp_data_price_sort]

