import os


def create_unique_filename():
    # Check if the file already exists, if yes, increase number in file name
    used_number_counter = 0
    parentDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    csv_file_name = os.path.join(parentDirectory,
                                 'steam_data',
                                 'steam_game_ids',
                                 'steam_game_ids{}.csv')
    while os.path.isfile(csv_file_name.format(used_number_counter)):
        used_number_counter += 1
    csv_file_name = csv_file_name.format(used_number_counter)
    return csv_file_name