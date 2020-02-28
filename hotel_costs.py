import requests
import bs4
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_hotel_costs(location, travel_dates):
    '''
    Hotel prices from Booking, Expedia, Agoda and HotelsCom2

    Inputs:
        travel_dates: (tuple) check in and check out dates, in YYYY-M-DD
        location: the city where the hotel is in
    '''

    check_in_date, check_out_date = travel_dates
    driver = webdriver.Chrome()
    driver.get('https://www.tripadvisor.com/Hotels')
    hotel_in = driver.find_element_by_xpath(('//*[@id="taplc_trip_search_home_'
                                            'hotels_0"]/div[2]/div[1]/div/span'
                                            '/input'))
    hotel_in.send_keys(location)
    driver.find_element_by_xpath('//*[@id="SUBMIT_HOTELS"]').click()
    time.sleep(2)
    # I gave up trying to use Selenium to find all links of hotels,
    # switching to beautifulsoup
    #hotels = driver.find_element_by_xpath('//*[@id="BODYCON"]/div[3]/div[3]')
    #hotels = hotels.find_element_by_css_selector('div')
    
    hotels_url = driver.current_url
    hotels_html = requests.get(hotels_url).text
    soup = bs4.BeautifulSoup(hotels_html, "html5lib")
    hotels = soup.find_all('div', id=('taplc_hsx_hotel_list_lite_dusty_hotels_'
                                      'combined_sponsored_0'))[0]
    hotels = hotels.find_all('div', class_=('prw_rup '
                                            'prw_meta_hsx_responsive_listing '
                                            'ui_section listItem'))
    hotel_key_corr = {}
    for hotel in hotels:
        url = 'https://www.tripadvisor.com'
        url += hotel.find_all('a')[0]['href']
        driver.get('https://xotelo.com/how-to-get-hotel-key.html')
        url_in = driver.find_element_by_xpath(('//*[@id="tripadvisor_url_'
                                               'input"]'))
        url_in.send_keys(url)
        driver.find_element_by_xpath(('/html/body/div[1]/div/div/form/div/span'
                                      '/button')).click()
        hotel_key = driver.find_element_by_xpath('//*[@id="url_result"]/code')
        hotel_key = hotel_key.text
        hotel_key_corr[hotel] = hotel_key

    list_responses = []
    for key in hotel_key_corr.values():
        print(key)
        url = ('https://data.xotelo.com/api/rates?hotel_key={}&chk_in={}'
               '&chk_out={}'.format(key, check_in_date, check_out_date))
        time.sleep(1)
        response = requests.get(url)
        # just for testing purposes
        if response.status_code == 200:
            print('Request Successful')
        else:
            print('Something is not right')
        list_responses.append(response.json())
    
    return list_responses

# test case
# one test id just in case: g60763-d2218992
get_hotel_costs('Chicago', ('2019-12-1', '2019-12-2'))