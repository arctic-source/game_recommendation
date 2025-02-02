import os

"""
Placeholder file to keep constants such as column names or paths to project files.
"""

NUMERICAL_DATA = ['price_eur', 'release_date', 'steam_rating', 'total_overall_reviews', 'positive_overall_reviews',
                  'total_recent_reviews', 'positive_recent_reviews']
TEXT_DATA = ['title', 'game_description']
CATEGORICAL_DATA = ['app_tags', 'genres', 'is_free_to_play', 'developers', 'publishers', 'nominal_overall_reviews',
                    'nominal_recent_reviews']
ID_DATA = ['url', 'steam_id']

COLUMNS_TO_DROP = ['nominal_overall_reviews', 'nominal_recent_reviews', 'total_recent_reviews',
                   'positive_recent_reviews', 'steam_id', 'url', 'game_description']
NUMERICAL_COLUMNS_FOR_SIMILARITY_CALCULATION = ['price_eur', 'release_date', 'steam_rating', 'total_overall_reviews',
                                                'positive_overall_reviews']
COLUMNS_TO_ONE_HOT_ENCODE = ['app_tags']

NUM_RECOMMENDATIONS = 5

# path management
UI_PATH = os.path.join("data", "ui_files", "steam_ui.ui")
STEAM_GAME_DATA = os.path.join("data", "steam_data", 'steam_game_data', "steam_dataset.feather")
ICON_PATH = os.path.join('data', 'icons', 'icon.png')
ANIMATIONS_PATH = os.path.join('data', 'animations', 'best')
BLANK_THUMBNAIL_PATH = os.path.join('data', 'steam_data', 'steam_thumbnails', '_blank.jpg')
THUMBNAILS_PATH = os.path.join('data', 'steam_data', 'steam_thumbnails')
LOADING_GIF_PATH = os.path.join('data', 'animations', 'loading_heavy_breathing.gif')
