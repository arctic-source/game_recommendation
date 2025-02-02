from src.back_end.steam_webscraping.scrape_a_game_by_url.reviews.extract_nominal_overall import extract_nominal_overall
from src.back_end.steam_webscraping.scrape_a_game_by_url.reviews.extract_nominal_recent import extract_nominal_recent
from src.back_end.steam_webscraping.scrape_a_game_by_url.reviews.extract_numeric_overall import extract_numeric_overall
from src.back_end.steam_webscraping.scrape_a_game_by_url.reviews.extract_numeric_recent import extract_numeric_recent
from src.back_end.steam_webscraping.scrape_a_game_by_url.reviews.helpers.no_reviews_check import no_reviews_check
from src.back_end.steam_webscraping.scrape_a_game_by_url.reviews.helpers.too_few_reviews_check import too_few_reviews_check
from src.back_end.steam_webscraping.scrape_a_game_by_url.reviews.helpers.too_few_reviews_correction import \
    too_few_recent_reviews_correction, too_few_overall_reviews_correction
from src.back_end.steam_webscraping.scrape_a_game_by_url.reviews.helpers.unpack_dict import unpack_dict


def scrape_reviews(soup, reviews_type):
    if reviews_type == 'recent':
        nominal_reviews = extract_nominal_recent(soup)
        numeric_reviews = extract_numeric_recent(soup)
    else:
        nominal_reviews = extract_nominal_overall(soup)
        numeric_reviews = extract_numeric_overall(soup)
    reviews = {
        "nominal_reviews": nominal_reviews,
        "total_reviews": numeric_reviews[0],
        "positive_reviews": numeric_reviews[1],
        "positive_reviews_percentage": numeric_reviews[2],
    }

    too_few_reviews = too_few_reviews_check(nominal_reviews)
    no_reviews = no_reviews_check(soup)

    if no_reviews:
        reviews.update(
            {
                "nominal_reviews": None,
                "total_reviews": None,
                "positive_reviews": None,
                "positive_reviews_percentage": None,
            }
        )
    elif too_few_reviews:
        if reviews_type == 'recent':
            reviews = too_few_recent_reviews_correction(reviews)
        else:
            reviews = too_few_overall_reviews_correction(reviews)

    return unpack_dict(reviews)
