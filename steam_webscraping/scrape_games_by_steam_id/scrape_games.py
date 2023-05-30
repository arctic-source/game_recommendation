import json
import os
import time

from steam_webscraping.process_html.helpers.fetch_existing_game_ids import fetch_existing_game_ids
from steam_webscraping.scrape_a_game_by_url.scrape_a_game_by_url import scrape_a_game_by_url
from steam_webscraping.scrape_games_by_steam_id.helpers.construct_link import construct_link
from steam_webscraping.scrape_games_by_steam_id.helpers.process_steam_id import process_steam_id

SLEEP_TIME = 0.15  # sec

file_with_steam_ids = os.path.join('..', '..', 'steam_data', 'steam_game_ids', 'steam_game_ids.csv')
path_with_scraped_ids = os.path.join('..', '..', 'steam_data', 'steam_game_data')

# Load IDs to be scraped, load IDs of games that were already scraped
game_ids = fetch_existing_game_ids(file_with_steam_ids)
scraped_game_ids_raw = os.listdir(path_with_scraped_ids)
scraped_game_ids = []
for scraped_game_id in scraped_game_ids_raw:
    id = process_steam_id(scraped_game_id)
    scraped_game_ids.append(id)

# difference of lists: game_ids - scraped_game_ids
game_ids_to_scrape = []
for element in game_ids:
    if element not in scraped_game_ids:
        game_ids_to_scrape.append(element)


# Perform web scraping of single steam websites
for id_str in game_ids_to_scrape:
    t_start = time.time()
    url = construct_link(id_str)
    game_data = scrape_a_game_by_url(url, suppress_request_print=True)

    # Write game data to json file
    steam_id = game_data['steam_id']
    json_file_name = str(steam_id) + '.json'
    json_full_file_name = os.path.join('..', '..', 'steam_data', 'steam_game_data', json_file_name)
    with open(json_full_file_name, 'w') as f:
        json.dump(game_data, f)
        time.sleep(SLEEP_TIME)
    disp_num_game = str(game_ids.index(str(steam_id))+1)
    disp_all_games = str(len(game_ids))
    t_end = time.time()
    t_per_game = str(t_end - t_start)
    print('Scraping game: ' + disp_num_game + r'/' + disp_all_games + ' (time per scrape: ' + t_per_game + ' s)')
