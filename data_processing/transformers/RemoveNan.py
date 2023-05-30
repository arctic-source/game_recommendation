from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

from data_processing.helpers.check_if_nans_exist import check_if_nans_exist
from data_processing.helpers.columns_that_contain_lists import columns_that_contain_lists


class RemoveNan(BaseEstimator, TransformerMixin):
    def __init__(self, keep_nans_in_columns, suppress_output):
        self.keep_nans_in_columns = keep_nans_in_columns
        self.suppress_output = suppress_output

    def fit(self, dataset: pd.DataFrame, y=None):
        return self
    def transform(self, dataset: pd.DataFrame, y=None):
        """ This function removes all instances that have a NaN or None in all attributes that are not listed in the keep_nans_in_columns variable """
        print('Removing nans...')
        nans_exist = check_if_nans_exist(dataset, self.suppress_output)
        if nans_exist:
            all_columns = dataset.columns
            columns_with_lists = columns_that_contain_lists(dataset)
            columns_to_remove_nans_from = list(set(all_columns) - set(self.keep_nans_in_columns))
            # drop items with nan values
            dataset = dataset.dropna(subset=columns_to_remove_nans_from)
            # drop items with empty lists
            for column_with_lists in columns_with_lists:
                if column_with_lists in columns_to_remove_nans_from:
                    # drop empty items (empty e.g. length of list is zero)
                    dataset = dataset[dataset[column_with_lists].map(lambda d: len(d)) > 0]
        return dataset