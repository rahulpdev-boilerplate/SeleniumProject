from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'C:\\Users\\Rahul\\PycharmProjects\\chromedriver.exe'

URL = 'https://secure-retreat-92358.herokuapp.com/'

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url=URL)


# item = driver.find_element_by_css_selector('#articlecount a')
# item = driver.find_element_by_link_text('anyone can edit')
item = driver.find_element_by_name('fName')
# item.click()
item.send_keys('Python')
item = driver.find_element_by_name('lName')
item.send_keys('Snake')
item = driver.find_element_by_name('email')
item.send_keys('python-snake@gmail.com')
item = driver.find_element_by_css_selector('form button')
item.send_keys(Keys.ENTER)

# print(item)
# print(item.tag_name)
# print(item.text)

# driver.quit()
