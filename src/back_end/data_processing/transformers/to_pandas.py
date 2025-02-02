from typing import Optional, List
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class ToPandas(BaseEstimator, TransformerMixin):
    """
    A transformer that converts a raw dataset (list or array-like) into a Pandas DataFrame.

    This transformer ensures that data is structured into a DataFrame with optional column
    and index labels.

    Attributes:
        columns (Optional[List[str]]): List of column names for the resulting DataFrame.
        index (Optional[List]): List of index labels for the resulting DataFrame.

    Methods:
        fit(dataset_raw, y=None):
            Returns the transformer instance (no fitting required).

        transform(dataset_raw, y=None):
            Converts the input list or array-like data into a Pandas DataFrame.
    """

    def __init__(self, columns: Optional[List[str]] = None, index: Optional[List] = None):
        """
        Initializes the ToPandas transformer.

        Args:
            columns (Optional[List[str]]): Column names for the resulting DataFrame. Defaults to None.
            index (Optional[List]): Index labels for the resulting DataFrame. Defaults to None.
        """
        self.columns = columns
        self.index = index

    def fit(self, dataset_raw, y=None):
        """
        Fit method for scikit-learn compatibility. Does nothing and returns self.

        Args:
            dataset_raw: Input dataset (ignored).
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            ToPandas: Returns self.
        """
        return self

    def transform(self, dataset_raw, y=None) -> pd.DataFrame:
        """
        Converts a raw dataset (list or array-like) into a structured Pandas DataFrame.

        Args:
            dataset_raw: The input dataset to be converted into a DataFrame.
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            pd.DataFrame: The transformed dataset as a Pandas DataFrame.
        """
        dataset_pandas = pd.DataFrame(dataset_raw, columns=self.columns,
                                      index=self.index)  # create DataFrame with optional column/index labels
        return dataset_pandas
