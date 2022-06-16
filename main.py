from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("/home/kaz/github/streaming/chromedriver")
#driver = webdriver.Chrome()
driver.get('https://www.2embed.ru/library/tv/253')

def get_episodes(season):
    episode_dropdown = driver.find_element(By.ID, f'ss-episodes-{season}')
    episode_dropdown.click()
    episodes = driver.find_elements(By.PARTIAL_LINK_TEXT, 'Episode')
    link_numbers = []
    episode_names = []
    for i in episodes:
        episode_names.append([i.text])
    episode_links = []
    for i in episode_names:
        ep_number = i[0].split(":")
        ep_number = ep_number[0].strip()
        ep = driver.find_element(By.PARTIAL_LINK_TEXT, ep_number)
        ep.click()
        link = driver.find_element(By.ID, "direct-link").get_attribute("value")
        link_numbers.append(link)
        episode_dropdown.click()
    for i in range(len(link_numbers)):
        episode_names[i].append(link_numbers[i])
        episode_names[i].insert(0,season)

    return episode_names


season_dropdown = driver.find_element(By.CLASS_NAME, 'edit-season')
season_dropdown.click()
seasons = driver.find_elements(By.PARTIAL_LINK_TEXT, "Season")
season_numbers = []
season_num = 1
for i in seasons:
    season_numbers.append(str(season_num))
    season_num +=1
final_links = []
temp_links = []
episode_names = []
for i in season_numbers:
    season_select = driver.find_element(By.PARTIAL_LINK_TEXT, f"Season {i}")
    season_select.click()
    temp_links = get_episodes(i)
    final_links = final_links + temp_links
    season_dropdown.click()
for i in final_links:
    print(i)