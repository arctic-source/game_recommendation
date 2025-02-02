from bs4 import BeautifulSoup


def extract_nominal_overall(soup: BeautifulSoup):
    # Extract game title (e.g. "Very Positive)
    overall_reviews = None
    too_few_overall_reviews = False

    REVIEW_IDENTIFIER = 'data-tooltip-html'
    OVERALL_REVIEW_KEYWORD = 'for this game'
    review_div_all = soup.find_all('span', {'class': 'game_review_summary'})
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
            if contains_overall_review_info:
                overall_reviews = review_div.text




    # # Check if there are too few reviews to extract a meaningful nominal overall review
    # if overall_reviews is not None:
    #     if overall_reviews[0].isdigit():
    #         too_few_overall_reviews = True
    #         overall_reviews = overall_reviews.split()[0]  # split '5 user reviews' into ['5', 'user', 'reviews']

    return overall_reviews

