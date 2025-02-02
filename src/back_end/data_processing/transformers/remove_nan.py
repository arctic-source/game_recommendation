from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
from src.back_end.data_processing.helpers.check_if_nans_exist import check_if_nans_exist
from src.back_end.data_processing.helpers.columns_that_contain_lists import columns_that_contain_lists


class RemoveNan(BaseEstimator, TransformerMixin):
    """
    A transformer that removes rows containing NaN or None values from a dataset.

    This transformer checks for NaN values and removes rows where NaNs appear in
    columns not listed in `keep_nans_in_columns`. It also removes rows with empty lists
    in specified columns.

    Attributes:
        keep_nans_in_columns (list): List of column names where NaNs are allowed.
        suppress_output (bool): Whether to suppress output when checking for NaNs.

    Methods:
        fit(dataset, y=None):
            Returns the transformer instance (no fitting required).

        transform(dataset, y=None):
            Removes rows with NaNs or empty lists based on specified rules.
    """

    def __init__(self, keep_nans_in_columns, suppress_output):
        """
        Initializes the RemoveNan transformer.

        Args:
            keep_nans_in_columns (list): List of column names where NaNs should be retained.
            suppress_output (bool): If True, suppresses printed output when checking for NaNs.
        """
        self.keep_nans_in_columns = keep_nans_in_columns
        self.suppress_output = suppress_output

    def fit(self, dataset: pd.DataFrame, y=None):
        """
        Fit method for scikit-learn compatibility. Does nothing and returns self.

        Args:
            dataset (pd.DataFrame): The input dataset (ignored).
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            RemoveNan: Returns self.
        """
        return self

    def transform(self, dataset: pd.DataFrame, y=None) -> pd.DataFrame:
        """
        Removes rows with NaNs from the dataset, except in specified columns.

        Args:
            dataset (pd.DataFrame): The input dataset.
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            pd.DataFrame: The dataset with NaN values and empty lists removed.
        """
        nans_exist = check_if_nans_exist(dataset, self.suppress_output)  # check if NaN values exist in the dataset

        if nans_exist:
            all_columns = dataset.columns  # get all column names
            columns_with_lists = columns_that_contain_lists(dataset)  # identify columns containing lists
            columns_to_remove_nans_from = list(
                set(all_columns) - set(self.keep_nans_in_columns))  # identify columns where NaNs should be removed

            # drop rows that contain NaN values in specified columns
            dataset = dataset.dropna(subset=columns_to_remove_nans_from)

            # remove rows with empty lists in relevant columns
            for column_with_lists in columns_with_lists:
                if column_with_lists in columns_to_remove_nans_from:
                    dataset = dataset[
                        dataset[column_with_lists].map(lambda d: len(d)) > 0]  # retain rows where lists are not empty

        return dataset
