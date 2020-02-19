import requests
# using an api from whatismyapiaddress.com
# api calls limited to once per 5 minute
# ip_response = requests.get('http://bot.whatismyipaddress.com')
# ip_address = ip_response.text

# alternative API, unlimited calls, but this level of convenience makes me
# question the legitimacy of the website
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
print(city, lat, lon)

# need to consider what happens when there is no internet connection