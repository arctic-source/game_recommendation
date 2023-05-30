import csv
import json

from steam_webscraping.scrape_a_game_by_url.scrape_a_game_by_url import scrape_a_game_by_url

with open('steam_game_ids3.csv', mode='r') as f:
    steam_id_list = []
    reader = csv.reader(f)
    for steam_id in reader:
        if steam_id is not None:
            steam_id_list.append(steam_id)
            url = r'https://store.steampowered.com/app/' + str(steam_id)
            game_data = scrape_a_game_by_url(steam_game_url=url, suppress_request_print=True)
            json_file_name = r'steam_data/' + str(steam_id) + '.json'
            with open(json_file_name, 'w') as f:
                json.dump(game_data, f)
            json.dump(game_data, open(json_file_name, 'w' ) )
