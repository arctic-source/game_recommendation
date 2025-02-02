from bs4 import BeautifulSoup


def extract_tags(soup: BeautifulSoup):
    app_tags = [tag.text.strip() for tag in soup.select('.app_tag')]
    if len(app_tags) != 0:
        try:
            app_tags.remove('+')
        except:
            pass
    return app_tags
