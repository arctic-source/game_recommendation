from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class DateToNumeric(BaseEstimator, TransformerMixin):
    """
    A transformer that converts a date column to a numeric format (days since a reference date).

    The reference date is set to "01 Jan 1970" (Unix epoch start), and all dates are
    transformed into the number of days since that reference.

    Methods:
        fit(dataset, y=None):
            Returns the transformer instance (no fitting required).

        transform(dataset, y=None):
            Converts the 'release_date' column to numeric format.

    """

    def fit(self, dataset: pd.DataFrame, y=None):
        """
        Fit method for scikit-learn compatibility. Does nothing and returns self.

        Args:
            dataset (pd.DataFrame): The input dataset (ignored).
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            DateToNumeric: Returns self.
        """
        return self

    def transform(self, dataset: pd.DataFrame, y=None) -> pd.DataFrame:
        """
        Transforms the 'release_date' column into the number of days since "01 Jan 1970".

        Args:
            dataset (pd.DataFrame): The input dataset containing a 'release_date' column.
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            pd.DataFrame: The transformed dataset with the 'release_date' column converted to numeric.
        """
        reference_year = pd.to_datetime('01 Jan 1970', format='%d %b %Y')
        dataset['release_date'] = (dataset['release_date'] - reference_year).dt.days
        return dataset
