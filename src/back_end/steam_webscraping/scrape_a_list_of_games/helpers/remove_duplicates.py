def remove_duplicates(input_list: list) -> list:
    list_without_duplicates = list(dict.fromkeys(input_list))
    return list_without_duplicates
