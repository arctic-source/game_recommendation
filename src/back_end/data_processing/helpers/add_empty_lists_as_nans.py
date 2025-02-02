import pandas as pd

from src.back_end.data_processing.helpers.columns_that_contain_lists import columns_that_contain_lists


def add_empty_lists_as_nans(dataset: pd.DataFrame, dataset_value_isna: pd.DataFrame):
    """Find elements of pandas dataframe that are empty lists and convert them to NaNs."""
    columns = dataset.columns
    columns_with_lists = columns_that_contain_lists(dataset)
    for column in columns:
        if column in columns_with_lists:
            dataset_value_isna[column] = dataset[column].apply(lambda x: len(x) == 0)
    return dataset_value_isna
