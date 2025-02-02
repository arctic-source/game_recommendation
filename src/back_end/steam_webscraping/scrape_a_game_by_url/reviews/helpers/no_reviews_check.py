from bs4 import BeautifulSoup


def no_reviews_check(soup: BeautifulSoup):
    no_reviews_tag = None
    no_reviews = False
    no_reviews_tag = soup.find('div', {'class': 'summary column'})
    if no_reviews_tag is not None:
        review_text = no_reviews_tag.text.strip().lower()
        if 'no' in review_text:
            no_reviews = True
    return no_reviews