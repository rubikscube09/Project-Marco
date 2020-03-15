#import util
#import weather_data
import requests
import bs4
import queue
import json
import language
import sys
import csv
import pandas as pd
from geopy.geocoders import Nominatim
import re

#FIX DATES
df=pd.read_csv("Scraping/destinations.csv")
df=df.iloc[1:]

#save_city_to_country_in_dict
def city_to_country(city):
    '''
    Matches city to country using the geopy api. 

    Input: string, city
    Output: string, no_country if none of the countries matches the city name.
    '''
    try:
        geolocator = Nominatim(user_agent='marco')
        location = geolocator.geocode(city, language='en-US')
        country = location.address.split(',')[-1].strip()
        if country == "United States of America":
            country = "United States"
        if country == "Jamaika":
            country = "Jamaica"
        return(country)
    except:
        #Hardcode a few stubborn cases
        if city=='hanoi':
            return('Vietnam')
        if city=='maputo':
            return('Mozambique')
        else:
            return("no_country")

def fill_country(df):
    '''
    fills in the country and city info into the pandas dataframe.
    Input: df: pandas datafraome
    Output: None
    '''
    df['country']=df.apply(lambda row: city_to_country(row['city']), axis=1)
    df['city']=df.apply(lambda row: row['city'].capitalize(), axis=1)


#Hardcode some cases from best available sources
language_dict=language.percent_dict
language_dict['Vietnam']=53.8
language_dict['Norway']=90
language_dict['Japan']=25
language_dict['Dominican Republic']=15
language_dict['Iceland']=90
language_dict['Uruguay']=10
language_dict['Ecuador']=35
language_dict['The Netherlands']=95


def get_language(country):
    '''
    Getting the country's corresponding language information from language_dict,

    Input: string: name of a country
    Output: string: the corresponding language if the country's name is within the\
    dictionary. Otherwise return No data
    '''
    try:
        return(language_dict[country])
    except:
        print(country)
        return("No data")


def fill_language(df):
    '''
    Adding the language information gotten from the last function into a pandas dataframe.
    Input: pandas dataframe
    Output: None
    '''
    df['language']=df.apply(lambda row: get_language(row['country']), axis=1)


def get_safety_info(starting_url):
    '''
    Scrapes the travel advisory info on the State Department website and
    gives a list containing nation name and advisory level.

    Input: a string of url
    Output: list
    '''
    
    filename = 'Travel Advisories.html'
    html = open(filename).read()
    soup = bs4.BeautifulSoup(html, "html.parser")
    table = soup.find_all("table")
    tr_list = table[0].find_all("tr")
    travel_advisory = {}
    for tr in tr_list:
        td = tr.find_all("td")
        if td != [] and td[0].text != "Worldwide Caution":
            td = td[ : -1]
            list_td = td[0].text.split()
            list_td = list_td[ : -2]
            td[0] = " ".join(list_td)
            td[1] = td[1].text
            travel_advisory[td[0]]=td[1]
    return travel_advisory


travel_advisory=get_safety_info('https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories.html/')

def get_safety(country):
    '''
    For any added country, get the travel advisory level of such country.

    Input: string
    Output: string, Level 1: Exercise Normal Precautions if the country is not in the keys of dictionary.
    '''

    try:
        return(travel_advisory[country])
    except:
        return('Level 1: Exercise Normal Precautions')

def fill_safety(df):
    df['safety']=df.apply(lambda row: get_safety(row['country']), axis=1)


def get_flight_costs(df, travel_dates, starting_dest):
    '''
    Get best flights to each destination, add to dataframe
    '''

    airports = pd.read_csv('airports.csv')
    airports.dropna(subset=['iata_code'], inplace=True)
    airports = airports[(airports['type'] == 'medium_airport') | (airports['type'] == 'large_airport')]
    # maybe output to new csv up to this point?
    airports = airports[airports['municipality'] == starting_dest]
    airports = airports['ident']
    # calucalte the closet airport by using current location
    origin = None
    # get destination from another function maybe
    destination = None
    # date is in MM/DD/YYYY format
    starting_date, return_date = travel_dates
    url = ('https://api.skypicker.com/flights?fly_from={}&fly_to={}'
           '&date_from={}&date_to={}&partner=picky&v=3'.format(origin, destination, starting_date, return_date))
    flight_response = requests.get(url)
    flight_data = flight_response.json()['data']
    output_df = pd.DataFrame()
    list_carriers = []
    prices = []
    list_duration = []
    for data in flight_data:
        airline = data['airlines'][0]
        price = data['price']
        duration = data['fly_duration']
        # the next line may not be right as there might be more than one route?
        flight_no = airline + str(data['route'][0]['flight_no'])
        list_carriers.append(flight_no)
        prices.append(price)
        list_duration.append(duration)
    
    output_df['flight'] = list_carriers
    output_df['price'] = prices
    output_df['duration'] = list_duration
    # the repsonse from API seems already sorted, but just to be sure
    output_df.sort_values(by=['price','duration'], inplace=True)
    return output_df


def get_hotel_costs(df, travel_dates):
    '''
    Get best hotels in each dest, add to dataframe
    Hotel prices from Booking, Expedia, Agoda and HotelsCom2
    '''

    base_url = 'https://data.xotelo.com/api/rates'
    # sample check in and check out dates
    check_in_date = '2020-2-13'
    check_out_date = '2020-2-15'
    # sample hotel key, need function to get hotel key (from Tripadvisor)
    hotel_key = 'g187791-d316644'
    request_url = base_url + '?hotel_key=' + hotel_key 
    request_url += '&chk_in=' + check_in_date
    request_url += '&chk_out=' + check_out_date
    response = requests.get(request_url)
    return response.json()

    
