import re
import util
import bs4
import queue
import json
import sys
import csv

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

def get_weather(df, travel_dates):
    '''
    Add weather info to dataframe.
    '''

def get_languages(df):
    '''
    Add language info to dataframe.
    '''

def get_safety(starting_url):
    '''
	Scrapes the travel advisory info on the State Department website and \
	gives a list containing nation name and advisory level.

	Input: a string of url
	Output: list
	'''
	request = util.get_request(starting_url)
	current_url = util.get_request_url(request)
	html = util.read_request(request)
	soup = bs4.BeautifulSoup(html, "html5lib")
	table = soup.find_all("table")
	tbody = table[0].find_all("tbody")
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

def get_hotel_costs(df, travel_dates):
    '''
    Get best hotels in each dest, add to dataframe
    '''
#FUNCTIONS TO POPULATE TREE
class tree:
    '''
    Leaves are vacations. Nodes are answers to questions above.
    '''

def populate_tree(df):
    '''
    Returns: tree object
    '''

def query_tree:
    '''
    Query our tree and return relevant info.
    '''
    
