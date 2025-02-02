from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class ParseDates(BaseEstimator, TransformerMixin):
    """
    A transformer that converts a date column into a standardized datetime format.

    This transformer parses the 'release_date' column from a string format into
    a Pandas datetime object using the format '%d %b %Y'.

    Methods:
        fit(dataset, y=None):
            Returns the transformer instance (no fitting required).

        transform(dataset, y=None):
            Converts the 'release_date' column to a Pandas datetime format.
    """

    def fit(self, dataset, y=None):
        """
        Fit method for scikit-learn compatibility. Does nothing and returns self.

        Args:
            dataset: The input dataset (ignored).
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            ParseDates: Returns self.
        """
        return self

    def transform(self, dataset, y=None):
        """
        Parses the 'release_date' column into a standardized datetime format.

        Args:
            dataset (pd.DataFrame): The input dataset containing a 'release_date' column.
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            pd.DataFrame: The dataset with the 'release_date' column converted to datetime.
        """
        dataset['release_date'] = pd.to_datetime(dataset['release_date'],
                                                 format='%d %b %Y')  # convert date strings to datetime format
        return dataset
