import requests

#Skyscanner API requests using Rapid-Api. 10 requests per day and then my credit card gets charged :^) .

url = 'https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0/'

param_dict = {
    'outboundDate' : '2020-03-21', # Departure and Return date resp.
    'inboundDate' : '2020-03-27' ,
    'cabinClass' : 'business',
    'numChildren' : str(0) ,
    'numInfants' : str(0),
    'country' : 'US',
    'currency' : 'USD',
    'locale' : 'en-US' ,
    'originPlace' : 'ORD',
    'destinationPlace' : 'LHR',
    'numAdults' : 1, 
	}

headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "21a93f3e0emsh34914a994184bdep12923cjsnc90566e5ca81",
    'content-type': "application/x-www-form-urlencoded"
    }

payload = "inboundDate={inboundDate}&cabinClass={cabinClass}&children={numChildren}&infants={numInfants}&country={country}\
&currency={currency}&locale={locale}&originPlace={originPlace}-sky&destinationPlace={destinationPlace}-sky&outboundDate={outboundDate}\
&adults={numAdults}".format(**param_dict)

response = requests.request('POST', url, headers=headers, data=payload)

resp_headers = response.headers

session_key = resp_headers['location'].rsplit("/").pop()

url = 'https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/uk2/v1.0/' + session_key

querystring = {'pageIndex':'0','pageSize':'10'}

headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "21a93f3e0emsh34914a994184bdep12923cjsnc90566e5ca81",
   }
response2 = requests.request('GET',url,headers=headers,params =querystring)