from bs4 import BeautifulSoup


def extract_genres(soup:BeautifulSoup):
    # Find official genres of game, e.g. ["Action", "Adventure", "RPG", "Casual"]
    genres = []
    genres_div = soup.find("div", id="genresAndManufacturer")
    if genres_div is not None:
        genre_span = genres_div.find("span")
        if genre_span is not None:
            genre_links = genre_span.find_all("a")
            if genre_links is not None:
                if len(genre_links) != 0:
                    for link in genre_links:
                        genres.append(link.text)
    return genres