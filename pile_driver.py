from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox(executable_path='./geckodriver')
driver.get('https://www.lonelyplanet.com/places')

drop_menu_select = Select(driver.find_element_by_class_name('jsx-60980745'))
drop_menu_select.select_by_visible_text('Cities')

cities = driver.find_elements_by_class_name('jsx-942575951')
cities[0].click()

driver.find_element_by_class_name('jsx-2155847788')

'''

drop_menu=driver.find_element_by_class_name('https://www.lonelyplanet.com/places')
drop_menu.click()
select = Select(driver.find_element_by_)





	jsx-60980745")

driver.find_elements_by_class_name(""jsx-942575951) #first 10
#loop thing.click()
''''