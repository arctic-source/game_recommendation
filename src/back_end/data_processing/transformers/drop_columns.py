from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
from typing import List


class DropColumns(BaseEstimator, TransformerMixin):
    """
    A transformer that drops specified columns from a Pandas DataFrame.

    Attributes:
        columns (List[str]): A list of column names to be dropped.

    Methods:
        fit(dataset, y=None):
            Returns the transformer instance (no fitting required).

        transform(dataset, y=None):
            Drops specified columns from the dataset.
    """

    def __init__(self, columns: List[str]):
        """
        Initializes the DropColumns transformer.

        Args:
            columns (List[str]): The list of column names to be dropped.
        """
        self.columns = columns

    def fit(self, dataset: pd.DataFrame, y=None):
        """
        Fit method for scikit-learn compatibility. Does nothing and returns self.

        Args:
            dataset (pd.DataFrame): The input dataset (ignored).
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            DropColumns: Returns self.
        """
        return self

    def transform(self, dataset: pd.DataFrame, y=None) -> pd.DataFrame:
        """
        Drops the specified columns from the dataset.

        Args:
            dataset (pd.DataFrame): The input dataset.
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            pd.DataFrame: The dataset with specified columns removed.
        """
        dataset = dataset.drop(columns=self.columns)
        return dataset
