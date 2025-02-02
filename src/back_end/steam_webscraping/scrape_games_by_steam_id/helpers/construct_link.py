def construct_link(id) -> str:
    base_link = r'https://store.steampowered.com/app/'
    id = str(id)
    link = base_link + id
    return link
