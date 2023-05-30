from bs4 import BeautifulSoup


def extract_game_description(soup: BeautifulSoup):
    game_description = None
    game_description_tag = soup.find("div", {'class': 'game_description_snippet'})
    if game_description_tag is not None:
        game_description = game_description_tag.text.strip()
    return game_description
