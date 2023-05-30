def find_image_link(soup):
    img_tag = soup.find('img', {'class': 'game_header_image_full'})
    img_link = img_tag['src']
    return img_link
