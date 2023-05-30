import pandas as pd

from data_processing.helpers.add_empty_lists_as_nans import add_empty_lists_as_nans


def check_if_nans_exist(dataset: pd.DataFrame, suppress_output: bool):
    nans_exist = False

    # Count nan or missing values
    if not suppress_output:
        print('')
        print('Missing (nan or empty) elements')

    # Find nan elements
    dataset_value_isna = dataset.isna()

    # Find elements with empty lists (consider them nan elements too)
    dataset_value_isna = add_empty_lists_as_nans(dataset, dataset_value_isna)

    # Find if nans exist
    columns = dataset.columns
    for column in columns:
        num_missing = dataset_value_isna[column].sum()
        if num_missing != 0:
            nans_exist = True
        if not suppress_output:
            print(f'{column}: {num_missing}')
    if not suppress_output:
        print(f'NaN values exist: {nans_exist}')

    return nans_exist
