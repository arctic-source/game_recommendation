def process_steam_id(raw_id: str) -> int:
    processed_id = raw_id.split('.')
    id = processed_id[0]
    # id = int(processed_id)
    return id
