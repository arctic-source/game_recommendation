import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from steam_webscraping.scrape_a_list_of_games.helpers.duplicates_exist import duplicates_exist
from steam_webscraping.scrape_a_list_of_games.helpers.create_unique_filename import create_unique_filename
from steam_webscraping.scrape_a_list_of_games.helpers.remove_duplicates import remove_duplicates
from steam_webscraping.scrape_a_list_of_games.helpers.scrape_single_steam_id import scrape_single_steam_id


def scrape_steam_game_ids(scroll_pause_time=3, approx_num_games_to_scrape=500):
    options = Options()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=options)

    STEAM_WEBSITE = r'https://store.steampowered.com/search/?supportedlang=english&ndl=1'
    print('Scraping a list of games (steam IDs of games) from the list of steam games, available on:')
    print(STEAM_WEBSITE)
    driver.get(STEAM_WEBSITE)
    driver.maximize_window()

    previous_html_elements_with_game_links = []
    steam_game_id_list = []
    scroll_num = 0
    num_of_steam_ids = 0
    csv_file_name = create_unique_filename()

    while True:

        # Scroll down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        scroll_num += 1

        # Scrape Steam ID
        steam_id, html_elements_with_any_links, steam_game_id_list = scrape_single_steam_id(
            driver, previous_html_elements_with_game_links, csv_file_name, steam_game_id_list)
        previous_html_elements_with_game_links = html_elements_with_any_links
        num_of_steam_ids = len(steam_game_id_list)
        # Wait to avoid website overload
        time.sleep(scroll_pause_time)
        print('scroll: ' + str(scroll_num) + ' (' + str(num_of_steam_ids) + ' games)')

        # Check if enough game IDs collected
        if num_of_steam_ids >= approx_num_games_to_scrape:
            break

    # Inform user
    print('Game Steam IDs scraped:')
    print(num_of_steam_ids)
    print('All IDs unique:')
    print(duplicates_exist(steam_game_id_list))
    print('')
    print('Steam game IDs were saved to:')
    print(csv_file_name)

    # # Check if IDs are unique again, remove duplicates
    # if duplicates_exist(steam_game_id_list):
    #     remove_duplicates(steam_game_id_list)

    driver.quit()
    return
