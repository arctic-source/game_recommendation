from bs4 import BeautifulSoup


def extract_nominal_recent(soup: BeautifulSoup):
    # Extract game title (e.g. "Very Positive)
    recent_reviews = None

    REVIEW_IDENTIFIER = 'data-tooltip-html'
    RECENT_REVIEW_KEYWORD = 'in the last 30 days'
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

            contains_recent_review_info = RECENT_REVIEW_KEYWORD in review_text
            if contains_recent_review_info:
                recent_reviews = review_div.text

    return recent_reviews
