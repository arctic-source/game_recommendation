import json
import os
import time
import pandas as pd

from data_processing.helpers.placeholders import GAME_FOLDER, JSON_GAME_FOLDER


def load_dataset(suppress_output=False, format_='csv'):

    if not suppress_output:
        print('Loading dataset ... ')

    current_file_path = os.path.abspath(__file__)
    file_list_with_full_path = []
    if format_ == 'csv':
        game_folder = GAME_FOLDER
    elif format_ == 'json':
        game_folder = JSON_GAME_FOLDER
    data_path = os.path.join(os.path.dirname(current_file_path), '../..', game_folder)
    file_list = os.listdir(data_path)
    for file_name in file_list:
        full_path = os.path.join(data_path, file_name)
        file_list_with_full_path.append(full_path)

    steam_dataset = []

    if format_ == 'csv':
        start = time.time()
        expected_list_types = {
            'app_tags': list,
            'genres': list,
            'developers': list,
            'publishers': list
        }
        # Load the dataset from csv
        steam_dataset = pd.read_csv(filepath_or_buffer=file_list_with_full_path[0],
                                    sep=';'
                                    )

        # Correct the data type
        for column_name, data_type in expected_list_types.items():
            steam_dataset[column_name] = steam_dataset[column_name].apply(eval)

        end = time.time()
        tot_time = end - start

    elif format_ == 'json':
        count_loaded_files = 0
        print_progress = 1000 # every 1000 games loaded
        start = time.time()
        for file_name in file_list_with_full_path:
            # Load a single data instance from JSON
            with open(file_name, 'r') as f:
                single_game_data = json.load(f)
                steam_dataset.append(single_game_data)
                count_loaded_files += 1
                if count_loaded_files % print_progress == 0:
                    print(count_loaded_files)
        end = time.time()
        tot_time = end - start

    if not suppress_output:
        print('Steam dataset loading time:')
        print(str(tot_time))
        print('Number of instances:')
        print(len(steam_dataset))

    return steam_dataset
