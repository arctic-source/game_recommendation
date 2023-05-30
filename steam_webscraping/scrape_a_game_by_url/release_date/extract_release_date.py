from bs4 import BeautifulSoup


def extract_release_date(soup: BeautifulSoup):
    release_date = soup.find('div', {'class':'date'})
    if release_date is None:
        return release_date
    release_date = release_date.text
    release_date = release_date.replace(',', '')
    return release_date