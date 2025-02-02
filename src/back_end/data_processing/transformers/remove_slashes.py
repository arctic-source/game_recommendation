from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import ast


class RemoveSlashes(BaseEstimator, TransformerMixin):
    """
    A transformer that removes backslashes from list-type columns in a dataset.

    This transformer identifies columns that contain lists, converts them to string
    format, removes backslashes, and then converts them back to lists using
    `ast.literal_eval`.

    Methods:
        fit(dataset, y=None):
            Returns the transformer instance (no fitting required).

        transform(dataset, y=None):
            Identifies list-type columns, removes backslashes, and converts strings back to lists.
    """

    def fit(self, dataset: pd.DataFrame, y=None):
        """
        Fit method for scikit-learn compatibility. Does nothing and returns self.

        Args:
            dataset (pd.DataFrame): The input dataset (ignored).
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            RemoveSlashes: Returns self.
        """
        return self

    def transform(self, dataset: pd.DataFrame, y=None) -> pd.DataFrame:
        """
        Identifies list-type columns, removes backslashes, and converts them back to lists.

        Args:
            dataset (pd.DataFrame): The input dataset containing list-type columns.
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            pd.DataFrame: The dataset with backslashes removed from list-type columns.
        """

        # identify columns that contain lists
        columns_containing_lists = []
        column_names = dataset.columns
        first_instance = dataset.iloc[0]  # check the first row to determine column types
        for column_name in column_names:
            first_instance_data_element = first_instance[column_name]
            is_list = isinstance(first_instance_data_element, list)  # check if data type is a list
            if is_list:
                columns_containing_lists.append(column_name)

        # remove backslashes from string representations of lists and convert back to lists
        for column_with_lists in columns_containing_lists:
            dataset[column_with_lists] = dataset[column_with_lists].astype(str)  # convert lists to string format
            dataset[column_with_lists] = dataset[column_with_lists].apply(
                ast.literal_eval)  # convert strings back to lists

        return dataset
