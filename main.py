from selenium import webdriver
import time

#driver = webdriver.Chrome("/home/kaz/github/streaming/chromedriver")
driver = webdriver.Chrome()
driver.get('https://www.2embed.ru/library/tv/253')

def get_episodes(season):
    episode_dropdown = driver.find_element_by_id('ss-episodes-'+season)
    episode_dropdown.click()
    episodes = driver.find_elements_by_partial_link_text('Episode')
    ep_number = 0
    link_numbers = []
    for i in episodes:
        link_numbers.append(str(ep_number))
        ep_number +=1
    episode_links = []
    for i in link_numbers:
        try:
            ep =driver.find_element_by_partial_link_text("Episode "+i)
            ep.click()
            link = driver.find_element_by_id("direct-link").get_attribute("value")
            episode_links.append(link)
            episode_dropdown.click()
        except:
            continue
    return episode_links
season_dropdown = driver.find_element_by_class_name('edit-season')
season_dropdown.click()
seasons = driver.find_elements_by_partial_link_text("Season")
season_numbers = []
season_num = 1
for i in seasons:
    season_numbers.append(str(season_num))
    season_num +=1
print(season_numbers)
final_links = []
temp_links = []
for i in season_numbers:
    season_select = driver.find_element_by_partial_link_text("Season "+i)
    season_select.click()
    temp_links = get_episodes(i)
    for j in temp_links:
        final_links.append(j)
    season_dropdown.click()
print(final_links)