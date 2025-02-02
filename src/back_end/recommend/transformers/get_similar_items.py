from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class FetchSimilarItems(BaseEstimator, TransformerMixin):
    """
    A transformer that fetches the most similar items based on similarity scores.

    This transformer selects the top `num_recommendations` items with the highest similarity
    scores, excluding the most similar one (which is assumed to be the input item itself).

    Attributes:
        num_recommendations (int): The number of recommended items to return.

    Methods:
        fit(dataset, y=None):
            Returns the transformer instance (no fitting required).

        transform(dataset, y=None):
            Selects and returns the top `num_recommendations` most similar items.
    """

    def __init__(self, num_recommendations: int):
        """
        Initializes the FetchSimilarItems transformer.

        Args:
            num_recommendations (int): The number of similar items to fetch.
        """
        self.num_recommendations = num_recommendations

    def fit(self, dataset: pd.DataFrame, y=None):
        """
        Fit method for scikit-learn compatibility. Does nothing and returns self.

        Args:
            dataset (pd.DataFrame): The input dataset (ignored).
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            FetchSimilarItems: Returns self.
        """
        return self

    def transform(self, dataset: pd.DataFrame, y=None) -> pd.DataFrame:
        """
        Fetches the most similar items based on the 'weighted_similarity' score.

        The highest similarity item is excluded as it is assumed to be the input item.

        Args:
            dataset (pd.DataFrame): The input dataset containing 'weighted_similarity' scores.
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            pd.DataFrame: A subset of the dataset with the top `num_recommendations` similar items.
        """

        # sort items by similarity score in descending order
        similarity_score = dataset['weighted_similarity'].astype(float).sort_values(ascending=False)

        # exclude the most similar item (assumed to be the input item itself)
        highest_similarity_score = similarity_score.iloc[1:self.num_recommendations + 1]

        # get indices of the highest similarity scores
        index_of_highest_similarity_score = list(highest_similarity_score.index)

        # retrieve the recommended items from the dataset
        recommended_items = dataset.loc[index_of_highest_similarity_score]

        return recommended_items
