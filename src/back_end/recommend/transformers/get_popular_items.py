from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class FetchPopularItems(BaseEstimator, TransformerMixin):
    """
    A transformer that fetches the most popular items based on the total number of positive reviews.

    This transformer selects the top `num_recommendations` items with the highest `total_positive_reviews`.

    Attributes:
        num_recommendations (int): The number of popular items to return.

    Methods:
        fit(dataset, y=None):
            Returns the transformer instance (no fitting required).

        transform(dataset, y=None):
            Selects and returns the top `num_recommendations` most popular items.
    """

    def __init__(self, num_recommendations: int):
        """
        Initializes the FetchPopularItems transformer.

        Args:
            num_recommendations (int): The number of popular items to fetch.
        """
        self.num_recommendations = num_recommendations

    def fit(self, dataset: pd.DataFrame, y=None):
        """
        Fit method for scikit-learn compatibility. Does nothing and returns self.

        Args:
            dataset (pd.DataFrame): The input dataset (ignored).
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            FetchPopularItems: Returns self.
        """
        return self

    def transform(self, dataset: pd.DataFrame, y=None) -> pd.DataFrame:
        """
        Fetches the most popular items based on the 'total_positive_reviews' column.

        Args:
            dataset (pd.DataFrame): The input dataset containing 'total_positive_reviews'.
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            pd.DataFrame: A subset of the dataset with the top `num_recommendations` popular items.
        """

        # sort items by total positive reviews in descending order
        popularity_score = dataset['total_positive_reviews'].astype(float).sort_values(ascending=False)

        # select the top `num_recommendations` popular items
        highest_popularity_score = popularity_score.iloc[:self.num_recommendations]

        # get indices of the highest popularity scores
        index_of_highest_popularity_score = list(highest_popularity_score.index)

        # retrieve the recommended popular items from the dataset
        recommended_items = dataset.loc[index_of_highest_popularity_score]

        return recommended_items
