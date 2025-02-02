import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def add_cos_similarity_column(instance: pd.Series, dataset: pd.DataFrame, similarity_name: str) -> pd.DataFrame:
    """
    Given instance (game) and dataset (all games), calculates cosine similarity between instance and all items from
    dataset, and saves those in a new column.
    Args:
        instance (pd.Series): single game data from Steam
        dataset (pd.DataFrame): data of all scraped games from Steam
        similarity_name (str): name of a similarity measure used

    Returns:
        dataset (pd.DataFrame): dataset with an extra column that represents calculated similarity measures of all games
        vs target game
    """
    # calculates the cosine similarity of instance with every other instance in the dataset
    dataset_numpy = dataset.to_numpy()
    instance_numpy = instance.to_numpy()
    similarity_array = cosine_similarity(instance_numpy, dataset_numpy)
    if similarity_name != '':
        new_column_name = f'{similarity_name}_similarity'
    else:
        new_column_name = 'similarity'
    dataset[new_column_name] = similarity_array.transpose()
    return dataset


def cos_similarity_non_optimized(array1, array2):
    """
    Naive way how to calculate cosine similarity. Works but is not optimized for speed.
    """
    return np.dot(array1, array2) / (np.linalg.norm(array1) * np.linalg.norm(array2))
