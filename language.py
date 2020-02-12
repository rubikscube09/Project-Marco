'''
Code for getting percentage of English speaker by country, outputs a json/
dictionary. Could modify to include more information.
'''

import bs4
import json
import re

filename = 'List countries English-speaking population.html'
html = open(filename, encoding='cp437').read()
soup = bs4.BeautifulSoup(html, "html5lib")
table = soup.find_all("table", class_='wikitable sortable')
body = table[0].find_all("tbody")
tag_countries = body[0].find_all('tr')
percent_dict = {}
for tag_country in tag_countries[2:-1]:
    data = tag_country.find_all('td')
    country = data[0].find_all('a')[0].text
    percentage = data[3].text.strip()
    percentage = re.findall(r'^\d{0,2}|\.\d{1,2}', percentage)
    percentage = ''.join(percentage)
    percent_dict[country] = percentage

with open('language.json', 'w') as file:
    json.dump(percent_dict, file)