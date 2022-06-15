from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://www.2embed.ru/library/tv/253')
time.sleep(5)
episode_dropdown = driver.find_element_by_id('ss-episodes-1')
episode_dropdown.click()
time.sleep(5)
episodes = driver.find_elements_by_partial_link_text('Episode')
ep_number = 0
link_numbers = []
for i in episodes:
    link_numbers.append(str(ep_number))
    ep_number +=1
print(link_numbers)
for i in link_numbers:
    ep =driver.find_element_by_partial_link_text("Episode "+i)
    ep.click()
    time.sleep(.5)
    link = driver.find_element_by_id("direct-link")
    print(link)
    episode_dropdown.click()
    time.sleep(.5)