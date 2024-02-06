from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time

URL = 'https://www.python.org/'
attribute = 'placeholder'
x_path = '//*[@id="site-map"]/div[2]/div/ul/li[3]/a'
CHROME_DRIVER_PATH = 'C:\\Users\\Rahul\\PycharmProjects\\chromedriver.exe'

# Create Selenium driver and open URL in Chrome browser
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(url=URL)

# item = driver.find_element_by_class_name('a-price')
# item = driver.find_element_by_name('q')
# item = driver.find_element_by_css_selector('.documentation-widget a')
# item = driver.find_element_by_xpath(x_path)

# item.click()
# time.sleep(2)
# item.send_keys('Python')
# item.send_keys(Keys.ENTER)

# print(item)
# print(item.tag_name)
# print(item.text)
# print(item.get_attribute(attribute))

# driver.quit()
