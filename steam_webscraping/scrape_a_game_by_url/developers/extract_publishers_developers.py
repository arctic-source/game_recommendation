from bs4 import BeautifulSoup


def extract_publishers_developers(soup: BeautifulSoup):
    # Find all elements with class "grid_label"
    grid_labels = soup.find_all(class_='grid_label')

    # Find the element with text "Publisher"
    developers = []
    publishers = []
    multiple_publishers = False
    multiple_developers = False
    publisher_label = None
    developer_label = None
    for label in grid_labels:
        if label.text == 'Publisher':
            publisher_label = label
        if label.text == 'Developer':
            developer_label = label

    if publisher_label is not None:
        # Find the next sibling element with class "grid_content"
        publisher_content = publisher_label.find_next_sibling(class_='grid_content')
        if publisher_content is not None:
            publishers_raw = publisher_content.text.strip()
            publishers_raw = publishers_raw.split(', ')
            publishers.extend(publishers_raw)


    if developer_label is not None:
        # Find the next sibling element with class "grid_content"
        developer_content = developer_label.find_next_sibling(class_='grid_content')
        if developer_content is not None:
            developers_raw = developer_content.text.strip()
            developers_raw = developers_raw.split(', ')
            developers.extend(developers_raw)

    return developers, multiple_developers, publishers, multiple_publishers