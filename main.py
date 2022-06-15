from selenium import webdriver
import time

driver = webdriver.Chrome("/home/kaz/github/streaming/chromedriver")

driver.get('https://www.2embed.ru/library/tv/253')
#time.sleep(.1)

def get_episodes():
    episode_dropdown = driver.find_element_by_id('ss-episodes-1')
    episode_dropdown.click()
    #time.sleep(1)
    episodes = driver.find_elements_by_partial_link_text('Episode')
    ep_number = 0
    link_numbers = []
    for i in episodes:
        link_numbers.append(str(ep_number))
        ep_number +=1
    episode_links = []
    for i in link_numbers:
        ep =driver.find_element_by_partial_link_text("Episode "+i)
        ep.click()
        #time.sleep(.1)
        link = driver.find_element_by_id("direct-link").get_attribute("value")
        episode_links.append(link)
        episode_dropdown.click()
        #time.sleep(.1)
    print(episode_links)
get_episodes()