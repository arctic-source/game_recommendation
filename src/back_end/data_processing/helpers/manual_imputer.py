import numpy as np
import pandas as pd


def manual_imputer(dataset: pd.DataFrame) -> pd.DataFrame:
    """
    Imputes missing values in the dataset for popular games that tend to be omitted due to irregular web-scraping
    results.

    For popular games (those with high ratings or many user reviews), Steam may  alter its website formatting, resulting
    in NaN values during automated scraping.
    This function applies manual imputations to ensure these games are included in  the recommendation engine.

    Args:
        dataset (pd.DataFrame): A DataFrame of web-scraped Steam games, potentially missing popular titles due to NaN
                                values.

    Returns:
        pd.DataFrame: The DataFrame with manual imputations applied to popular game titles.
    """
    popular_games_fill_na = {
        'Grand Theft Auto V': {
            'price_eur': np.float64(29.98)
        },
        'EA SPORTS FIFA 23': {
            'price_eur': np.float64(20.99)
        },
        'Stumble Guys': {
            'price_eur': np.float64(0.0),
            'is_free_to_play': True
        },
        'Metro 2033 Redux': {
            'price_eur': np.float64(19.99)
        },
        'World War 3': {
            'price_eur': np.float64(0.0),
            'is_free_to_play': True
        },
        'Assassin’s Creed IV Black Flag': {
            'release_date': '19 Nov 2013'
        },
        'Metro: Last Light Redux': {
            'price_eur': np.float64(19.99)
        },
        'SPORE': {
            'price_eur': np.float64(19.99)
        },
        'Ori and the Blind Forest': {
            'price_eur': np.float64(19.99)
        },
        'Besiege': {
            'price_eur': np.float64(12.99)
        },
        'Max Payne 3': {
            'price_eur': np.float64(19.99)
        },
        'Super Animal Royale': {
            'is_free_to_play': True,
            'price_eur': np.float64(0.0)
        },
        'ATLAS': {
            'is_free_to_play': False,
            'price_eur': np.float64(24.99)
        },
        'Mass Effect Legendary Edition': {
            'price_eur': np.float64(59.99)
        },
        'Brothers - A Tale of Two Sons': {
            'price_eur': np.float64(14.99)
        },
        'The Elder Scrolls IV: Oblivion Game of the Year Edition Deluxe': {
            'price_eur': np.float64(14.99),
            'genres': ['RPG']
        },
        'Mafia II (Classic)': {
            'price_eur': np.float64(29.99)
        },
        'Bright Memory': {
            'price_eur': np.float64(6.59)
        },
        'Ryse: Son of Rome': {
            'price_eur': np.float64(9.99)
        },
        'A Way Out': {
            'price_eur': np.float64(29.99)
        },
        'Pacify': {
            'price_eur': np.float64(3.99)
        }
    }

    for game_title in popular_games_fill_na.keys():
        game = dataset[dataset['title'] == game_title]
        game_index = game.index[0]
        for key, value in popular_games_fill_na[game_title].items():
            dataset.loc[game_index, key] = value

    return dataset
