import request

import socket

def get_location():
    '''
    using an api from whatismyapiaddress.com to get the current location of the user
    api calls limited to once per 5 minute
    Input: None
    Output: None
    '''
    # the follwing part tests your internet connection
    connection = False
    try:
        # see if we can resolve the host name -- tells us if 
        # there is a DNS listening
        host = socket.gethostbyname("www.google.com")
        # connect to the host -- tells us if the host is actually reachable
        s = socket.create_connection((host, 80), 2)
        s.close()
        connection = True
    except:
        input('Please enter location:' )
    
    # alternative API, unlimited calls, but this level of convenience makes me
    # question the legitimacy of the website
    if connection == True:
        ip_response = requests.get('https://ifconfig.me/')
        ip_address = ip_response.text
    
        # using an api from ipstack.com
        # the string after ? is my api access token
    
        loc_request_url = 'http://api.ipstack.com/' + ip_address
        location_response = requests.get(loc_request_url + \
                                '?access_key=e24ee45fcafb4d395d01679458ac43dd')
        location_json = location_response.json()
        city = location_json['city']
        lat = location_json['latitude']
        lon = location_json['longitude']