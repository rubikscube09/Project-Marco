#Scrape city links from Lonely Planet.
#
#TEAM NAME: NOTE, SHOULD CHANGE LOCAL PATH FOR DRIVER
#

import time
import datetime
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

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

def clear_warnings():
	'''
	Clear warnings from site.
	'''

	click_past_class(driver, 'optanon-alert-box-bg')
	click_past_class(driver, 'optanon-allow-all')
	click_past_class(driver, 'optanon-popup-bg')

def scrape_cities(start_page, num_pages_to_scrape, csv_name):
	'''
	Get the names and the Lonely Planet URLs for cities on specified pages (each page contains the name of 12 cities, and cities appear across pages in order of popularity.)

	Inputs:
		start_page: page # to start scraping on
		num_pages_to_scrape: number of pages to scrape
		csv_name: CSV file for cities and URLs
	Returns:
		None (writes to CSV file)
	'''

	#Set up driver
	driver = webdriver.Firefox(executable_path='./geckodriver')
	driver.get('https://www.lonelyplanet.com/places')

	clear_warnings()

	#View destinations by city
	drop_menu_select = Select(driver.find_element_by_class_name('jsx-60980745'))
	drop_menu_select.select_by_visible_text('Cities')

	clear_warnings()

	#Get total number of pages of cities
	num_pages=int(driver.find_element_by_class_name('jsx-2286953760').find_elements_by_class_name('flex')[-1].find_element_by_class_name('mr-24').text[3:])

	assert start_page<num_pages and start_page+num_pages_to_scrape<num_pages	

	#Scrape pages and write to CSV
	for i in range(start_page+num_pages_to_scrape):

		#Navigate to start_page
		if i+1<start_page:
			click_past_xpath(driver, '/html/body/div[6]/div/main/section/section/div/p/span[3]/button')
		
		#Scrape num_pages_to_scrape pages
		else:
			time1=time.perf_counter()
			city_links=[]

			wait_for_class(driver, 'jsx-2155847788', total_wait=3)

			#Get Firefox elements for each city
			cities=[city for city in driver.find_elements_by_class_name('jsx-2155847788') if str(city.get_attribute("class"))=='jsx-2155847788 leading-tight']

			#Click on each city to get link
			for city in cities:
				c=wait_for_class(driver, "optanon-allow-all", total_wait=3)
				city.click()
				link=city.find_element_by_tag_name("a").get_attribute("href")
				city_links.append((capitalize(str(link.split("/")[-1]))),link)
			
			#Write city names and links to CSV
			with open(csv_name,'a+') as output:
			    csv_write=csv.writer(output)
			    for row in city_links:
			        csv_write.writerow(row)

			#Navigate to next page
			click_past_xpath(driver, '/html/body/div[6]/div/main/section/section/div/p/span[3]/button')
			
			#Report progress of scraping to use, and estimate of time remaining.
			time2=time.perf_counter()
			took=time2-time1
			time_left=str(datetime.timedelta(seconds=(num_pages-(start_page+i+1))*took))
			print('Pages crawled: '+str(start_page+i+1)+'/'+str(num_pages)+'\r')
			print('Time remaining: '+time_left+'\r')