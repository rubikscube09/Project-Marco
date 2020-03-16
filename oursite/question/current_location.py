import requests
import socket

def get_location():
    '''
    Test the user's internet location, if there is a connection, return the
    user's current location.

    Input: None

    Output: the current city or an empty string if there is no connection
    '''
    
    connection = False
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        s.close()
        connection = True
    except:
        return ''
    
    # alternative API
    if connection == True:
        ip_response = requests.get('https://ifconfig.me/')
        ip_address = ip_response.text
    
        # using an api from ipstack.com
        loc_request_url = 'http://api.ipstack.com/' + ip_address
        location_response = requests.get(loc_request_url + \
                                '?access_key=e24ee45fcafb4d395d01679458ac43dd')
        location_json = location_response.json()
        city = location_json['city']
        return city