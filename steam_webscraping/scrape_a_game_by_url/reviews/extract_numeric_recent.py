from bs4 import BeautifulSoup
import numpy as np

def extract_numeric_recent(soup: BeautifulSoup):
    total_reviews = np.nan
    positive_reviews_percentage = np.nan
    positive_reviews = np.nan
    too_few_reviews = False
    recent_reviews_unavailable = False

    RECENT_REVIEW_KEYWORD = 'in the last 30 days'
    REVIEW_IDENTIFIER = 'data-tooltip-html'
    TOO_FEW_REVIEWS_IDENTIFIER = 'Need more'
    review_div_all = soup.find_all('div', {'class': 'user_reviews_summary_row'})
    if review_div_all is not None and len(review_div_all) != 0:

        # extract review text
        review_div_list = []
        for potential_review_div in review_div_all:
            if potential_review_div.has_key(REVIEW_IDENTIFIER):
                # html element (review div) contains needed review information
                review_div = potential_review_div
                review_div_list.append(review_div)

        # check whether review information is about recent or overall reviews
        for review_div in review_div_list:
            review_text = review_div[REVIEW_IDENTIFIER]
            contains_recent_review_info = RECENT_REVIEW_KEYWORD in review_text
            too_few_reviews = TOO_FEW_REVIEWS_IDENTIFIER in review_text

            if contains_recent_review_info and not too_few_reviews:

                # extract number of recent and positive reviews
                total_reviews = review_text[review_text.find('the') + len('the'):review_text.rfind('user')]
                total_reviews = total_reviews.replace(',', '')
                total_reviews = total_reviews.strip()
                if total_reviews.isdigit():

                    total_reviews = int(total_reviews)

                    positive_reviews_percentage = int(review_text[:review_text.rfind('%')])

                    positive_reviews = int(positive_reviews_percentage * 0.01 * total_reviews)
    else:
        recent_reviews_unavailable = True

    return total_reviews, positive_reviews, positive_reviews_percentage, too_few_reviews, recent_reviews_unavailable

