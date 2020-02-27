#Scrape info from city pages on Lonely Planet.
#
#TEAM NAME: NOTE, SHOULD CHANGE LOCAL PATH FOR DRIVER
#

import time
import datetime
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import os

os.environ['MOZ_HEADLESS'] = '1'

def wait_for_class(driver, class_name, total_wait=5):
    '''
    Wait up to total_wait seconds for a class to appear.

    Inputs:
        driver: webdriver object
        class_name: name of target class
        total_wait: wait time in seconds
    Returns:
        None
    '''
    try:
        element=driver.find_element_by_class_name(class_name)
    except:
        total_wait -=1
        time.sleep(1)
        if total_wait>1:
            wait_for_class(driver, class_name, total_wait)

def click_past_class(driver, id_, total_wait=3):
    '''
    Wait up to total_wait seconds for a clickable class to appear, e.g. a button. Once it appears, click.

    Inputs:
        driver: webdriver object
        id: id of target
        total_wait: wait time in seconds
    Returns:
        None
    '''
    try:
            element=driver.find_element_by_class_name(id_).click()
    except:
            total_wait = total_wait-1
            time.sleep(1)
            if total_wait>1:
                    click_past_class(driver, id_, total_wait)

def click_past_xpath(driver, id_, total_wait=3):
    '''
    Wait up to total_wait seconds for a clickable class to appear, e.g. a button. Once it appears, click.

    Inputs:
        driver: webdriver object
        id: id of target
        total_wait: wait time in seconds
    Returns:
        None
    '''
    try:
            element=driver.find_element_by_xpath(id_).click()
    except:
            total_wait = total_wait-1
            time.sleep(1)
            if total_wait>1:
                    click_past_xpath(driver, id_, total_wait)

def clear_warnings(driver):
    '''
    Clear warnings from site.
    '''

    click_past_class(driver, 'optanon-alert-box-bg')
    click_past_class(driver, 'optanon-allow-all')
    click_past_class(driver, 'optanon-popup-bg')

def crawl_one_city(url):
    '''
    Scrape relevant info from one city page.

    Inputs:
        url: a url
    Returns:
        tuple: (string, image_link)
    '''
    #Set up driver
    driver = webdriver.Firefox(executable_path='./geckodriver')
    driver.get(url)

    clear_warnings(driver)

    click_past_xpath(driver, '/html/body/div[6]/div/div[2]/main/section[1]/div[2]/p/button')

    sections=[element.find_element_by_tag_name("p").text for element in driver.find_elements_by_class_name('jsx-3380108488') if element.get_attribute("class")=='jsx-3380108488 subsection' or element.get_attribute("class")=='jsx-3380108488 featured font-light']
    text_str=""
    for section in sections:
        text_str=text_str+" "+section
    
    image_link=driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/header/div[1]/picture').find_element_by_tag_name("source").get_attribute("data-srcset").split(", ")[-1]
    return(tuple((text_str, image_link)))

def crawl_cities_from_list(url_csv, start_city, num_cities, target_csv):
    '''
    Get key text and image from CSV containing city link.

    Inputs:
        url_csv: CSV with city names and URLs
        start_city: row of URL to start with
        num_cities: number of city pages to scrape
    Returns:
        pandas DataFrame
    '''
    df=pd.read_csv(url_csv, header=None, names=('city','url'), skiprows=start_city, nrows=num_cities)

    df['tuple']=df.apply(lambda row: crawl_one_city(row['url']), axis=1)
    df['description']=df.apply(lambda row: row['tuple'][0], axis=1)
    df['image']=df.apply(lambda row: row['tuple'][1], axis=1)

    del df['tuple']
    
    with open(target_csv, 'a+') as output:
        df.to_csv(output, header=False)