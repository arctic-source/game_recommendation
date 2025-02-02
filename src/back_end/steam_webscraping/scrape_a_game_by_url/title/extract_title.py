from bs4 import BeautifulSoup


def extract_title(soup: BeautifulSoup):
    # Extract game title (e.g. "Grand Theft Auto V")
    title = None
    title_tag = soup.find('div', {'id': 'appHubAppName_responsive'})
    if title_tag is not None:
        title = title_tag.text.strip()
    return title
