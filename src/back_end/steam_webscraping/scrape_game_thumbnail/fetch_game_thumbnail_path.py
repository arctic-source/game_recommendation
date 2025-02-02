import os

from src.back_end.placeholders import THUMBNAILS_PATH
from src.back_end.steam_webscraping.scrape_game_thumbnail.helpers.scrape_game_thumbnail import scrape_game_thumbnail


def fetch_game_thumbnail_path(steam_game_url: str) -> str:
    """
    Fetches the file path for the thumbnail of a given Steam game.

    This function takes a Steam game URL as input, scrapes the game's thumbnail using the
    scrape_game_thumbnail function, then constructs and returns the file path where the
    thumbnail image is saved. The file path is based on the current file's location,
    appended with 'steam_data' and 'steam_thumbnails' folders. The file name is the Steam ID
    of the game with a '.jpg' extension.

    The Steam ID is extracted from the game's URL. The function assumes that the URL has the
    form '.../apps/Steam_ID/' or '.../Steam_ID/...'.

    Parameters:
    steam_game_url (str): The URL of the Steam game for which to fetch the thumbnail path.

    Returns:
    str: The absolute path to where the thumbnail should be saved, including the file name.
    """
    scrape_game_thumbnail(steam_game_url)

    steam_id = None

    # extract steam id
    url_parts = steam_game_url.split('/')
    for i, url_part in enumerate(url_parts):
        if 'apps' in url_part:
            steam_id = url_parts[i+1]
            break
        elif url_part.isdigit():
            steam_id = url_part
            break
    save_file_name = steam_id + '.jpg'

    thumbnail_full_path = os.path.join(THUMBNAILS_PATH, save_file_name)
    return thumbnail_full_path
