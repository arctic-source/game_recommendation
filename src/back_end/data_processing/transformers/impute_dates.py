from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

from src.back_end.data_processing.helpers.custom_date_imputer import custom_date_imputer


class ImputeDates(BaseEstimator, TransformerMixin):
    """
    A transformer that imputes missing or incomplete dates using a custom date imputer.

    This transformer applies the `custom_date_imputer` function to the 'release_date' column
    to standardize or fill in missing day values.

    Methods:
        fit(dataset, y=None):
            Returns the transformer instance (no fitting required).

        transform(dataset, y=None):
            Applies the custom imputer to standardize dates.
    """

    def fit(self, dataset: pd.DataFrame, y=None):
        """
        Fit method for scikit-learn compatibility. Does nothing and returns self.

        Args:
            dataset (pd.DataFrame): The input dataset (ignored).
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            ImputeDates: Returns self.
        """
        return self

    def transform(self, dataset: pd.DataFrame, y=None) -> pd.DataFrame:
        """
        Applies the `custom_date_imputer` function to the 'release_date' column.

        Args:
            dataset (pd.DataFrame): The input dataset containing a 'release_date' column.
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            pd.DataFrame: The dataset with standardized dates.
        """
        dataset['release_date'] = dataset['release_date'].apply(custom_date_imputer)
        return dataset
