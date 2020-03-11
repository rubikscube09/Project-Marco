import re
import util
import weather_data
import requests
import bs4
import queue
import json
import sys
import csv
import pandas as pd

#FUNCTIONS TO FILL DATAFRAME
def get_destinations(starting_url,n):
    '''
    Crawl pages on lonely planet. Return a dataframe table with n vacation
    destinations, and the words assosciated with each vacation destination.
    '''

def get_keywords(destinations,j,k, df):
    '''
    Extract j non-common words that are best at binning the destinations into k
    bins above. Return a dataframe with only these key words.
    '''

def get_weather(df, city, travel_dates):
    '''
    Add weather info to dataframe.
    '''

    # call weather_data

    
def get_languages(df):
    '''
    Add language info to dataframe.
    '''

def get_safety(starting_url):
    '''
    Scrapes the travel advisory info on the State Department website and
    gives a list containing nation name and advisory level.

    Input: a string of url
    Output: list
    '''
    
    filename = 'Travel Advisories.html'
    html = open(filename).read()
    soup = bs4.BeautifulSoup(html, "html5lib")
    table = soup.find_all("table")
    tr_list = table[0].find_all("tr")
    travel_advisory = []
    for tr in tr_list:
        td = tr.find_all("td")
        if td != [] and td[0].text != "Worldwide Caution":
            td = td[ : -1]
            list_td = td[0].text.split()
            list_td = list_td[ : -2]
            td[0] = " ".join(list_td)
            td[1] = td[1].text
            travel_advisory.append(td)
    return travel_advisory

def get_flight_costs(df, travel_dates, starting_dest):
    '''
    Get best flights to each dest, add to dataframe
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

    # please find new version in hotel_costs.py

    
#FUNCTIONS TO POPULATE TREE
class tree:
    '''
    Leaves are vacations. Nodes are answers to questions above.
    '''

def populate_tree(df):
    '''
    Returns: tree object
    '''

def query_tree():
    '''
    Query our tree and return relevant info.
    '''
    
