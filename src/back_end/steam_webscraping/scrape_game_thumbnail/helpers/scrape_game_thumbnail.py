import requests
from bs4 import BeautifulSoup

from src.back_end.steam_webscraping.scrape_game_thumbnail.helpers.download_image import download_image
from src.back_end.steam_webscraping.scrape_game_thumbnail.helpers.find_image_link import find_image_link


def scrape_game_thumbnail(steam_game_url):
    page = requests.get(steam_game_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    img_link = find_image_link(soup)
    download_image(img_link)

# url = r'https://store.steampowered.com/app/236390/War_Thunder/'
# scrape_game_thumbnail(url)
