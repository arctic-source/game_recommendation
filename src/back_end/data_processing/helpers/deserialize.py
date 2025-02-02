from ast import literal_eval

import pandas as pd


def deserialize_df(df: pd.DataFrame):
    """
    When saving lists of values into csv, this needs de-serialization after reading the csv. E.g. converting
    "["my", "list", "elements"]" into ["my", "list", "elements"]
    Args:
        df: dataframe to deserialize

    Returns:
        df: dataframe with deserialized columns
    """
    expected_list_types = {
        'app_tags': list,
        'genres': list,
        'developers': list,
        'publishers': list
    }
    for column_name, data_type in expected_list_types.items():
        df[column_name] = df[column_name].apply(literal_eval)

    return df
