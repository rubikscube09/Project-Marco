'''
Code for getting percentage of English speaker by country, outputs a json/
dictionary. Could modify to include more information.
'''

import bs4
import json
import re

#Countries not appearing in list
CORRECTIONS_DIC={'Norway':95}

filename = 'List countries English-speaking population.html'

def fill_percent_dic():
    html = open(filename, encoding='cp437').read()
    soup = bs4.BeautifulSoup(html, "html5lib")
    table = soup.find_all("table", class_='wikitable sortable')
    body = table[0].find_all("tbody")
    tag_countries = body[0].find_all('tr')
    percent_dic={}
    for tag_country in tag_countries[2:-1]:
        data = tag_country.find_all('td')
        country = data[0].find_all('a')[0].text
        percentage = data[3].text.strip()
        percentage = re.findall(r'^\d{0,2}|\.\d{1,2}', percentage)
        percentage = ''.join(percentage)
        percent_dic[country] = percentage
    return(percent_dic)

PERCENT_DIC=fill_percent_dic()

def get_language(country):
    if country in PERCENT_DIC:
        return(PERCENT_DIC[country])
    elif country in CORRECTIONS_DIC:
        return(c)
    else:
        print("failed "+country)
        return(-1)