from sklearn.base import BaseEstimator, TransformerMixin


class ProcessSimilarItems(BaseEstimator, TransformerMixin):
    """
    A transformer that extracts the 'titles' column from the dataset.

    This transformer simply returns the 'titles' column, assuming it contains relevant
    information about similar items.

    Methods:
        fit(dataset, y=None):
            Returns the transformer instance (no fitting required).

        transform(dataset, y=None):
            Extracts and returns the 'titles' column.
    """

    def fit(self, dataset, y=None):
        """
        Fit method for scikit-learn compatibility. Does nothing and returns self.

        Args:
            dataset: The input dataset (ignored).
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            ProcessSimilarItems: Returns self.
        """
        return self

    def transform(self, dataset, y=None):
        """
        Extracts the 'titles' column from the dataset.

        Args:
            dataset: The input dataset containing a 'titles' column.
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            pd.Series: The extracted 'titles' column.
        """
        titles = dataset['titles']  # extract the 'titles' column
        return titles
