from bs4 import BeautifulSoup


def extract_steam_id(steam_game_url: str):
    steam_id = None

    url_parts = steam_game_url.split('/')
    steam_id = int(url_parts[url_parts.index('app')+1])
    try:
        steam_id = int(url_parts[url_parts.index('app') + 1])
    except:
        pass

    # start = 'app/'
    # try:
    #     steam_id = int(steam_game_url[steam_game_url.find(start) + len(start):])
    # except:
    #     steam_id = None

    # Using beautiful soup from appid from html content
    # appid = None
    # appid_input = soup.select_one('#review_appid')
    # if appid_input is not None:
    #     appid = appid_input['value']
    #     steam_id = appid
    return steam_id
