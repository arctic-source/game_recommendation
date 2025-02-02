from typing import List

import pandas as pd


def columns_that_contain_lists(dataset: pd.DataFrame) -> List[str]:
    """This function checks which columns have list as data types"""

    columns_that_contain_lists = []
    columns = dataset.columns
    for column in columns:
        first_row_data_type = type(dataset[column].loc[0])
        if first_row_data_type == list:
            columns_that_contain_lists.append(column)

    return columns_that_contain_lists
