import os


GAME_FOLDER = os.path.join('steam_data', 'steam_game_data')
JSON_GAME_FOLDER = os.path.join('steam_data', 'steam_game_data_json')

NUMERICAL_DATA = ['price_eur', 'release_date', 'steam_rating', 'total_overall_reviews', 'positive_overall_reviews', 'total_recent_reviews', 'positive_recent_reviews']
TEXT_DATA = ['title', 'game_description']
CATEGORICAL_DATA = ['app_tags', 'genres', 'is_free_to_play', 'developers', 'publishers', 'nominal_overall_reviews', 'nominal_recent_reviews']
ID_DATA = ['url', 'steam_id']

COLUMNS_TO_DROP = ['nominal_overall_reviews', 'nominal_recent_reviews', 'total_recent_reviews','positive_recent_reviews', 'steam_id', 'url', 'game_description']
NUMERICAL_COLUMNS_FOR_SIMILARITY_CALCULATION = ['price_eur', 'release_date', 'steam_rating', 'total_overall_reviews', 'positive_overall_reviews']
COLUMNS_TO_ONE_HOT_ENCODE = ['app_tags']