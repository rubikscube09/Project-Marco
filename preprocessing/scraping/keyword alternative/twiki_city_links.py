import bs4
import pandas as pd
import pickle
import requests
import re
import json


def get_cities():
    '''
    Get cities of interest from city_links_csv
    '''

    cities = pd.read_csv(r'..\city_links_csv.csv', header=None, \
                                                        keep_default_na=False)
    cities = cities.loc[:,0]
    with open('list_cities.txt', 'wb') as f:
        pickle.dump(cities, f)


def cap_city(name):
    '''
    Capitalize city name to match the url naming convention of wikitravel
    '''

    names = name.split('-')
    if len(names) == 1:
        name = names[0].capitalize()
    else:
        list_cap = []
        for n in names:
            cap_n = n.capitalize()
            list_cap.append(cap_n)
        name = '_'.join(list_cap)
    return name


def scrape(url):
    '''
    Given a url, scrape the things to see and do.
    I didn't bother scraping the lists since it seems difficult and I don't
    think we need info like benefits of new york city pass as keyword
    '''

    html = requests.get(url).text
    soup = bs4.BeautifulSoup(html, "html5lib")
    try:
        section = soup.select('#See')[0].parent
    except:
        redirect = soup.find_all('ul', class_='redirectText')[0]
        redirect = redirect.find_all('li')[0].find_all('a')
        redirect_link = 'https://wikitravel.org' + redirect[0]['href']
        html = requests.get(redirect_link).text
        soup = bs4.BeautifulSoup(html, 'html5lib')
        section = soup.select('#See')[0].parent
    output = {}
    name = 'See'
    subcategory = 'Description'
    subcat_dict = {}
    not_buy = True
    while not_buy:
        # since breaking involved using regular expressions, not sure how to 
        # move that into the while condition
        # NOTE: 1. work on removing the italicized stuff
        #       2. I am missing another deeper level here
        #           so I am not scraping anything for some pages
        # The city Arusha does not have tag SEE or DO, consider this
        if section.next_sibling != None:
            section = section.next_sibling
        else:
            section = section.parent
        if section.name == 'h2' or section.name == 'h3' or section.name == 'p':
            if section.name == 'h2':
                section_title = re.findall(r'(?<!\[)\b\w+\b(?![\]])', section.text)
                if section_title[0][:3] == 'Buy' or section_title[0][:3] == 'Eat':
                    not_buy = False
                    break
                elif section_title[0][:3] == 'Do':
                    name = 'Do'
                    subcategory = 'Description'
                    subcat_dict = {}
            if section.name == 'h3':
                subcategory = re.findall(r'(.*)\[', section.text)[0]
            elif section.name == 'p':
                if subcategory not in subcat_dict:
                    subcat_dict[subcategory] = section.text.strip()
                else:
                    subcat_dict[subcategory] += section.text.strip()

            output[name] = subcat_dict
            
    return output


def scrape_all(verbose=False):
    '''
    Find links and scrape everything.
    '''

    with open("list_cities.txt", "rb") as f:
        cities = pickle.load(f)

    cities = cities.apply(lambda name: cap_city(name))

    base_url = 'https://wikitravel.org/en/'

    city_data = {}
    count = 0
    for city in cities.array:
        if verbose:
            count += 1
            print('We have scraped {} cities'.format(count))
        print('Scraping', city)
        url = base_url + city
        html = requests.get(url).text
        # three cases might happen:
        # 1: we go directly to the page of the city
        # 2: there is no page found
        # 3: there are more than one city with that name
        soup = bs4.BeautifulSoup(html, "html5lib")
        empty_tag = soup.find_all('div', \
                                    class_ = 'noarticletext mw-content-ltr')
        # nothing found
        # NOTE: need to correct Rio_De_Janeiro to Rio_de_Janeiro,
        if len(empty_tag) == 1:
            print('Nothing here, buds!')
            city_data[city] = 'Not available'
            continue

        # more than one city
        multiple_tag = soup.find_all('a', title = "Category:Disambiguation")
        if len(multiple_tag) == 1:
            print('Multiple possible matches, might take some time...')
            possible_cities = soup.find_all('ul')
            for tag in possible_cities:
                list_cities = tag.find_all('li')
                for city in list_cities:
                # actually you should find list and then continue
                    if any(re.findall(r'city|town', city.text)):
                        # if the tag indeed leads to a city, get its url
                        link_tag =  tag.find_all('a')[0]
                        print(link_tag)
                        if link_tag.get('class') != None and link_tag.get('class')[0] != 'mw-selflink':
                            link = link_tag['href']
                            if 'action=edit' not in link:
                                # if the link is not a new page waiting to be edited
                                url = 'https://wikitravel.org/' + link
                                city_name = re.findall(r'^[^-]*[^ -]', tag.text)[0]
                                print('Scraping', city_name)
                                output = scrape(url)
                                city_data[city_name] = output
        else:
            # direct scraping
            print('Scraping directly, nice')
            city_data[city] = scrape(url)

        with open('city_data.json', 'w') as f:
            json.dump(city_data, f)

#scrape_all(True)