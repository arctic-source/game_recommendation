import pandas as pd

from src.back_end.data_processing.helpers.runtime_measure import measure_elapsed_time
from src.back_end.placeholders import STEAM_GAME_DATA


@measure_elapsed_time
def load_dataset(verbose=False) -> pd.DataFrame:
    """
    Load web-scraped dataset with Steam game data into memory. Optimized by using snappy parquet instead of csv.

    Args:
        verbose: Allow prints for debugging reasons etc.

    Returns:
        steam_dataset: A dataframe with web-scraped Steam games
    """

    if verbose:
        print('Loading dataset ... ')

    steam_dataset = pd.read_feather(STEAM_GAME_DATA)

    if verbose:
        print('Number of instances:')
        print(len(steam_dataset))

    return steam_dataset
