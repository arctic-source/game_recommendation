from src.back_end.steam_webscraping.scrape_a_list_of_games.scrape_list_of_games import scrape_steam_game_ids


SCROLL_PAUSE_TIME = 1.5
APPROX_NUM_GAMES_TO_SCRAPE = 80000
steam_game_id_list = scrape_steam_game_ids(scroll_pause_time=SCROLL_PAUSE_TIME,
                                           approx_num_games_to_scrape=APPROX_NUM_GAMES_TO_SCRAPE)
