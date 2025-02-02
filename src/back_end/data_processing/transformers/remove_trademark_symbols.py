from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class RemoveTrademarkSymbols(BaseEstimator, TransformerMixin):
    """
    A transformer that removes trademark symbols ('™' and '®') from the 'title' column.

    This transformer scans the 'title' column and removes unwanted symbols, ensuring
    clean and standardized text.

    Methods:
        fit(dataset, y=None):
            Returns the transformer instance (no fitting required).

        transform(dataset, y=None):
            Removes trademark symbols from the 'title' column.
    """

    def fit(self, dataset: pd.DataFrame, y=None):
        """
        Fit method for scikit-learn compatibility. Does nothing and returns self.

        Args:
            dataset (pd.DataFrame): The input dataset (ignored).
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            RemoveTrademarkSymbols: Returns self.
        """
        return self

    def transform(self, dataset: pd.DataFrame, y=None) -> pd.DataFrame:
        """
        Removes trademark symbols ('™' and '®') from the 'title' column.

        Args:
            dataset (pd.DataFrame): The input dataset containing a 'title' column.
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            pd.DataFrame: The dataset with trademark symbols removed from the 'title' column.
        """
        unwanted_characters = ['™', '®']

        for character in unwanted_characters:
            dataset['title'] = dataset['title'].str.replace(character, '', regex=False)  # remove trademark symbols

        return dataset
