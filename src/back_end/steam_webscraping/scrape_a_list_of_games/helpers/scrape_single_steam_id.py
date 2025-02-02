from csv import writer

from bs4 import BeautifulSoup


def scrape_single_steam_id(web_driver, previous_html_elements_with_game_links, csv_file_name, steam_ids):
    steam_id = None

    # Find html elements containing any links
    html_elements_with_any_links = web_driver.find_elements('xpath', '//a[@href]')
    num_of_new_elements = len(html_elements_with_any_links) - len(previous_html_elements_with_game_links)
    new_elements = html_elements_with_any_links[-num_of_new_elements:]
    for html_element in new_elements:
        html_content = html_element.get_attribute('innerHTML')

        if r'/apps/' in html_content or r'/app/' in html_content:
            soup = BeautifulSoup(html_content, 'html.parser')
            thumbnail_link = soup.find('img')['src']
            start = '/apps/'
            end = '/capsule_sm'
            steam_id = int(thumbnail_link[thumbnail_link.find(start) + len(start):thumbnail_link.rfind(end)])
            if steam_id is not None:
                if steam_id not in steam_ids:
                    with open(csv_file_name, mode='a', newline='') as f:
                        writer_object = writer(f, delimiter=',')
                        writer_object.writerow([steam_id])
                        steam_ids.append(steam_id)
                # else:
                #     print('Non-unique Steam ID found: ' + str(steam_id))
            else:
                print('A steam ID could not be scraped.')
    return steam_id, html_elements_with_any_links, steam_ids
