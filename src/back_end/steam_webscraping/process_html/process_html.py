import os

from bs4 import BeautifulSoup

from src.back_end.steam_webscraping.process_html.helpers.append_to_csv import append_to_csv
from src.back_end.steam_webscraping.process_html.helpers.fetch_existing_game_ids import fetch_existing_game_ids
from src.back_end.steam_webscraping.process_html.helpers.filter_text import filter_text

# File name of resulting csv with steam IDs
file_name_results = 'steam_game_ids.csv'
file_path_results = os.path.join('..', '..', 'steam_data', 'steam_game_ids', file_name_results)

# File names of mhtml batches
input_file_names = os.listdir(os.path.join('..', '..', 'steam_data', 'steam_game_list_html', 'batches'))

for i, input_file_name in enumerate(input_file_names):
    file_path = os.path.join('..', '..', 'steam_data', 'steam_game_list_html', 'batches', input_file_name)

    discovered_steam_ids = []

    with open(file_path, 'r') as f:
        print('Currently processing:')
        print(file_path)
        soup = BeautifulSoup(f, 'html.parser')

        # Find html elements containing any links
        html_elements_with_any_links = soup.find_all('a', {'href': True})
        for html_element in html_elements_with_any_links:
            link = html_element['href']
            LINK_KEYWORD = '/app/'
            keyword_present = filter_text(text=link, keyword=LINK_KEYWORD)
            if not keyword_present:
                continue
            # Split link to words
            link_words = link.split('/')
            for count, word in enumerate(link_words):
                if not word == 'app':
                    continue
                steam_id = link_words[count+1]
                steam_id = int(steam_id)
                # Check if this steam ID was already scraped
                already_scraped_ids = fetch_existing_game_ids(file_path_results)
                if steam_id not in already_scraped_ids:
                    discovered_steam_ids.append(steam_id)
                    append_to_csv(file_path_results, steam_id)
                break
    print('Batch no. ' + str(i))
    print('Steam IDs in this batch: ' + str(len(discovered_steam_ids)))
    print('Total Steam IDs: ' + str(len(already_scraped_ids)))
    print('')
