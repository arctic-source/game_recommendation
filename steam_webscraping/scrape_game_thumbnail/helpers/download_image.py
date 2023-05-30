import os.path

import requests


def download_image(url):
    steam_id = None
    thumbnail_downloaded = False

    current_path_and_filename = os.path.abspath(__file__)
    current_path = os.path.dirname(current_path_and_filename)
    project_path = os.path.abspath(os.path.join(current_path, '../..', '..'))
    save_folder_path = os.path.join(project_path, 'steam_data', 'steam_thumbnails')

    # extract steam id
    url_parts = url.split('/')
    for i, url_part in enumerate(url_parts):
        if 'apps' in url_part:
            steam_id = url_parts[i+1]
            break
        elif url_part.isdigit():
            steam_id = url_part
            break
    save_file_name = steam_id + '.jpg'

    save_folder_full_path_and_name = os.path.join(save_folder_path, save_file_name)

    downloaded_thumbnails = os.listdir(save_folder_path)
    if save_file_name in downloaded_thumbnails:
        thumbnail_downloaded = True

    if not thumbnail_downloaded:
        response = requests.get(url)
        if response.status_code == 200:
            img = response.content
            # wb .. write binary
            # rb .. read binary
            with open(save_folder_full_path_and_name, 'wb') as file:
                file.write(response.content)

