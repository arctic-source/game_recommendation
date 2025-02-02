from bs4 import BeautifulSoup
import numpy as np

def extract_numeric_overall(soup: BeautifulSoup):
    total_reviews = np.nan
    positive_reviews_percentage = np.nan
    positive_reviews = np.nan
    too_few_reviews = False
    overall_reviews_unavailable = False

    OVERALL_REVIEW_KEYWORD = 'for this game'
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
            contains_overall_review_info = OVERALL_REVIEW_KEYWORD in review_text
            too_few_reviews = TOO_FEW_REVIEWS_IDENTIFIER in review_text

            if contains_overall_review_info and not too_few_reviews:

                # extract number of overall and positive reviews
                total_reviews = review_text[review_text.find('the') + len('the'):review_text.rfind('user')]
                total_reviews = total_reviews.replace(',', '')
                total_reviews = total_reviews.strip()
                if total_reviews.isdigit():

                    total_reviews = int(total_reviews)

                    positive_reviews_percentage = int(review_text[:review_text.rfind('%')])

                    positive_reviews = int(positive_reviews_percentage * 0.01 * total_reviews)
            elif too_few_reviews:

                # extract number of overall reviews (positive unavailable if too few reviews)
                phrase_list_delimited_by_slash_n = review_div.text.strip().split('\n')
                for phrase in phrase_list_delimited_by_slash_n:
                    if 'user reviews' in phrase:
                        phrase_list_delimited_by_spaces = phrase.split(' ')
                        for phrase_ in phrase_list_delimited_by_spaces:
                            if phrase_.isdigit():
                                total_reviews = int(phrase_)
    else:
        overall_reviews_unavailable = True

    return total_reviews, positive_reviews, positive_reviews_percentage, too_few_reviews, overall_reviews_unavailable