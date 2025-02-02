def shorten_title_length(title: str) -> str:
    """If game title is longer than X characters, show the first X characters and show "..." after it"""
    longest_allowed_title = 34  # characters
    if len(title) >= longest_allowed_title:
        shortened_title = title[:longest_allowed_title] + ' ...'
    else:
        shortened_title = title
    return shortened_title
