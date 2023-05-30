import requests
from bs4 import BeautifulSoup

from steam_webscraping.scrape_a_game_by_url.developers.extract_publishers_developers import \
    extract_publishers_developers
from steam_webscraping.scrape_a_game_by_url.game_description.extract_game_description import extract_game_description
from steam_webscraping.scrape_a_game_by_url.genres.extract_genres import extract_genres
from steam_webscraping.scrape_a_game_by_url.price.extract_price import extract_price
from steam_webscraping.scrape_a_game_by_url.release_date.extract_release_date import extract_release_date
from steam_webscraping.scrape_a_game_by_url.reviews.extract_steam_rating import extract_steam_rating
from steam_webscraping.scrape_a_game_by_url.reviews.scrape_reviews import scrape_reviews
from steam_webscraping.scrape_a_game_by_url.steam_id.extract_steam_id import extract_steam_id
from steam_webscraping.scrape_a_game_by_url.tags.extract_tags import extract_tags
from steam_webscraping.scrape_a_game_by_url.title.extract_title import extract_title


def scrape_a_game_by_url(steam_game_url, suppress_request_print=False):
    game_data = {}

    if r'https://store.steampowered.com/app/' in steam_game_url:
        page = requests.get(steam_game_url)
        if not suppress_request_print:
            print(page.text)

        soup = BeautifulSoup(page.content, "html.parser")

        # Extract user reviews - recent and overall
        nominal_recent_reviews, total_recent_reviews, positive_recent_reviews, positive_recent_reviews_percentage = scrape_reviews(
            soup, "recent"
        )
        nominal_overall_reviews, total_overall_reviews, positive_overall_reviews, positive_overall_reviews_percentage = scrape_reviews(
            soup, "overall"
        )


        # More game details
        title = extract_title(soup)
        steam_rating = extract_steam_rating(soup)
        developers, multiple_developers, publishers, multiple_publishers = extract_publishers_developers(soup)
        app_tags = extract_tags(soup)
        genres = extract_genres(soup)
        price_euro, is_free_to_play = extract_price(soup, app_tags)
        steam_id = extract_steam_id(steam_game_url)
        release_date = extract_release_date(soup)
        game_description = extract_game_description(soup)

        game_data.update(
            {
                "url": steam_game_url,
                "steam_id": steam_id,
                "title": title,
                "app_tags": app_tags,
                "genres": genres,
                "is_free_to_play": is_free_to_play,
                "price_eur": price_euro,
                "release_date": release_date,
                "steam_rating": steam_rating,
                "nominal_overall_reviews": nominal_overall_reviews,
                "nominal_recent_reviews": nominal_recent_reviews,
                "total_recent_reviews": total_recent_reviews,
                "positive_recent_reviews": positive_recent_reviews,
                "total_overall_reviews": total_overall_reviews,
                "positive_overall_reviews": positive_overall_reviews,
                "developers": developers,
                "publishers": publishers,
                "game_description": game_description,
            }
        )
    return game_data