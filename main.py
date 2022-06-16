from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#driver = webdriver.Chrome("/home/kaz/github/streaming/chromedriver")
driver = webdriver.Chrome()
driver.get('https://www.2embed.ru/library/tv/253')

def get_episodes(season):
    episode_dropdown = driver.find_element(By.ID, f'ss-episodes-{season}')
    episode_dropdown.click()
    episodes = driver.find_elements(By.PARTIAL_LINK_TEXT, 'Episode')
    ep_number = 0
    link_numbers = []
    episode_names = []
    for i in episodes:
        link_numbers.append(str(ep_number))
        ep_number +=1
    episode_links = []
    for i in link_numbers:
        try:
            ep = driver.find_element(By.PARTIAL_LINK_TEXT, f"Episode {i}")
            ep.click()
            link = driver.find_element(By.ID, "direct-link").get_attribute("value")
            episode_links.append(link)
            episode_dropdown.click()
        except:
            continue
    return episode_links, episode_names


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
    temp_links, temp_names = get_episodes(i)
    final_links = final_links + temp_links
    episode_names = episode_names + temp_names
    season_dropdown.click()
for i in range(len(final_links)):
    print(final_links[i], episode_names[i])