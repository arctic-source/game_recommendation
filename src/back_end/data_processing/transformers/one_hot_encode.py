from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class OneHotEncode(BaseEstimator, TransformerMixin):
    """
    A transformer that performs one-hot encoding on specified categorical columns.

    This transformer expands categorical columns into binary one-hot encoded columns,
    ensuring proper handling of multi-label categorical values.

    Attributes:
        columns_to_one_hot_encode (list): List of column names to apply one-hot encoding.

    Methods:
        fit(dataset, y=None):
            Returns the transformer instance (no fitting required).

        transform(dataset, y=None):
            Applies one-hot encoding to the specified columns.
    """

    def __init__(self, columns):
        """
        Initializes the OneHotEncode transformer.

        Args:
            columns (list): List of column names to be one-hot encoded.
        """
        self.columns_to_one_hot_encode = columns

    def fit(self, dataset: pd.DataFrame, y=None):
        """
        Fit method for scikit-learn compatibility. Does nothing and returns self.

        Args:
            dataset (pd.DataFrame): The input dataset (ignored).
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            OneHotEncode: Returns self.
        """
        return self

    def transform(self, dataset: pd.DataFrame, y=None) -> pd.DataFrame:
        """
        Applies one-hot encoding to specified categorical columns.

        Args:
            dataset (pd.DataFrame): The input dataset containing categorical columns.
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            pd.DataFrame: The dataset with one-hot encoded columns added.
        """
        for column in self.columns_to_one_hot_encode:
            # explode multi-label categorical values into separate rows before encoding
            one_hot_encoded = pd.get_dummies(
                dataset[column].explode(),
                prefix=column, prefix_sep='_'
            )

            # sum one-hot encoded values by index to restore original DataFrame shape
            one_hot_encoded_grouped = one_hot_encoded.groupby(level=0).sum()

            # concatenate the new one-hot encoded columns with the original dataset
            dataset = pd.concat([dataset, one_hot_encoded_grouped], axis=1)

        return dataset
