def remove_duplicates(input: list) -> list:
    list_without_duplicates = list(dict.fromkeys(input))
    return list_without_duplicates