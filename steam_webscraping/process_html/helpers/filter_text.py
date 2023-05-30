def filter_text(text: str, keyword='/app'):
    keyword = '/app/'
    if keyword in text:
        return True
    return False
