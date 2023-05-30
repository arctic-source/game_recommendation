from bs4 import BeautifulSoup

from steam_webscraping.scrape_a_game_by_url.reviews.extract_nominal_overall import extract_nominal_overall
from steam_webscraping.scrape_a_game_by_url.reviews.helpers.too_few_reviews_check import too_few_reviews_check


def extract_steam_rating(soup:BeautifulSoup):
    steam_rating = None
    nominal_reviews = extract_nominal_overall(soup)
    too_few_overall_reviews = too_few_reviews_check(nominal_reviews)
    if not too_few_overall_reviews:
        rating_meta = soup.select_one('meta[itemprop="ratingValue"]')
        if rating_meta is not None:
            steam_rating = rating_meta.get('content')
    return steam_rating