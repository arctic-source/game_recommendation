import csv
import os

from src.back_end.steam_webscraping.scrape_a_list_of_games.helpers.duplicates_exist import duplicates_exist
from src.back_end.steam_webscraping.scrape_a_list_of_games.helpers.remove_duplicates import remove_duplicates


def fetch_existing_game_ids(file_path):
    steam_ids = []
    file_exists = os.path.exists(file_path)
    if file_exists:
        with open(file_path, 'r') as f:
            reader_object = csv.reader(f, delimiter=',')
            row_num = 0
            for row in reader_object:
                if not row == []:
                    steam_ids.append(row[0])
                    row_num += 1
                else:
                    continue
            # # Check if IDs are unique, remove duplicates
            if duplicates_exist(steam_ids):
                steam_ids = remove_duplicates(steam_ids)
    return steam_ids


def fetch_empty_list(file_path):
    return []

