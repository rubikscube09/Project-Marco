def fill_safety(starting_url):
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
    
TRAVEL_ADVISORY=fill_safety('https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories.html/')
CORRECTIONS={}
def get_safety(country):
    if country in CORRECTIONS:
        return(CORRECTIONS[country])
    elif country in TRAVEL_ADVISORY:
        return(TRAVEL_ADVISORY[country])
    else:
        return("Level 1: Exercise Normal Precautions")
