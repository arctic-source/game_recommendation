from sklearn.base import BaseEstimator, TransformerMixin
from src.back_end.data_processing.helpers.manual_imputer import manual_imputer


class ImputeManually(BaseEstimator, TransformerMixin):
    """
    A transformer that applies a manual imputation function to a dataset.

    This transformer uses the `manual_imputer` function to handle missing or incorrect
    values in the dataset.

    Methods:
        fit(dataset, y=None):
            Returns the transformer instance (no fitting required).

        transform(dataset, y=None):
            Applies the manual imputer to process the dataset.
    """

    def fit(self, dataset, y=None):
        """
        Fit method for scikit-learn compatibility. Does nothing and returns self.

        Args:
            dataset: The input dataset (ignored).
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            ImputeManually: Returns self.
        """
        return self

    def transform(self, dataset, y=None):
        """
        Applies the `manual_imputer` function to the dataset.

        Args:
            dataset: The input dataset that requires manual imputation.
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            The dataset after manual imputation.
        """
        dataset = manual_imputer(dataset)  # apply manual imputation to handle missing values
        return dataset
