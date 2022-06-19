from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#driver = webdriver.Chrome("/home/kaz/github/streaming/chromedriver")

def get_episodes(season, driver):
    episode_dropdown = driver.find_element(By.ID, f'ss-episodes-{season[-1]}')
    episode_dropdown.click()
    episodes = driver.find_elements(By.PARTIAL_LINK_TEXT, 'Episode')
    links = []
    episode_names = [[i.text] for i in episodes]
    episode_links = []
    for i in episode_names:
        ep_number = i[0].split(":")
        ep_number = ep_number[0].strip()
        ep = driver.find_element(By.PARTIAL_LINK_TEXT, ep_number)
        ep.click()
        link = driver.find_element(By.ID, "direct-link").get_attribute("value")
        links.append(link)
        episode_dropdown.click()
    for i in range(len(links)):
        episode_names[i].append(links[i])
        episode_names[i].insert(0,season)

    return episode_names

def start():
    driver = webdriver.Chrome()
    driver.get('https://www.2embed.ru/library/tv/655')
    season_dropdown = driver.find_element(By.CLASS_NAME, 'edit-season')
    season_dropdown.click()
    seasons = driver.find_elements(By.PARTIAL_LINK_TEXT, "Season")
    final_links = []
    temp_links = []
    for i in seasons:
        season = i.text
        season_select = driver.find_element(By.PARTIAL_LINK_TEXT, i.text)
        season_select.click()
        temp_links = get_episodes(season,driver)
        final_links = final_links + temp_links
        season_dropdown.click()
    return final_links
