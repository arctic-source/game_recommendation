from bs4 import BeautifulSoup


def extract_price(soup: BeautifulSoup, app_tags: list):
    price_eur = None
    price = None
    is_free_to_play = False

    regular_price = soup.find('div', class_='game_purchase_price price')
    if regular_price is None:
        return price_eur, is_free_to_play

    if 'free' in regular_price.text.strip().lower():
        is_free_to_play = True
        price = 0.0

    if not is_free_to_play:
        all_prices = soup.find_all('div', {'data-price-final': True})
        if all_prices == []:
            for tag in app_tags:
                if 'free to play' in tag.lower():
                    is_free_to_play = True
                    price_eur = 0.0
                    break
                return price_eur, is_free_to_play
        else:
            price = int(all_prices[0]['data-price-final'])
    if price is not None:
        price_eur = float(price) / 100
    return price_eur, is_free_to_play
