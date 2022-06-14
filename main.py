from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://projectfreetv.one/tv/star-trek-39401')
time.sleep(5)
iframe = driver.find_element_by_id("iframe-embed")
link = iframe.get_attribute('src')
driver.get(link)
time.sleep(2)
button = driver.find_element_by_id('play-now')
