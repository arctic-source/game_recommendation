from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class WeightedSimilarity(BaseEstimator, TransformerMixin):
    """
    A transformer that calculates a weighted similarity score using numerical and categorical similarity.

    This transformer computes a new column, 'weighted_similarity', as the weighted average of numerical
    and categorical similarity scores.

    Attributes:
        numerical_weight (float): The weight assigned to numerical similarity.
        categorical_weight (float): The weight assigned to categorical similarity.

    Methods:
        fit(dataset, y=None):
            Returns the transformer instance (no fitting required).

        transform(dataset, y=None):
            Computes the weighted similarity score and adds it as a new column.
    """

    def __init__(self, numerical_weight: float, categorical_weight: float):
        """
        Initializes the WeightedSimilarity transformer.

        Args:
            numerical_weight (float): The weight assigned to numerical similarity.
            categorical_weight (float): The weight assigned to categorical similarity.
        """
        self.numerical_weight = numerical_weight
        self.categorical_weight = categorical_weight

    def fit(self, dataset: pd.DataFrame, y=None):
        """
        Fit method for scikit-learn compatibility. Does nothing and returns self.

        Args:
            dataset (pd.DataFrame): The input dataset (ignored).
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            WeightedSimilarity: Returns self.
        """
        return self

    def transform(self, dataset: pd.DataFrame, y=None) -> pd.DataFrame:
        """
        Computes the weighted similarity score and adds it as a new column 'weighted_similarity'.

        The formula used is:
        ```
        weighted_similarity = (numerical_weight * num_similarity + categorical_weight * cat_similarity) / 2
        ```

        Args:
            dataset (pd.DataFrame): The input dataset containing 'num_similarity' and 'cat_similarity' columns.
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            pd.DataFrame: The dataset with the new column 'weighted_similarity'.
        """
        dataset['weighted_similarity'] = (
                (self.numerical_weight * dataset['num_similarity'] + self.categorical_weight * dataset[
                    'cat_similarity']) / 2
        )  # calculate weighted similarity score

        return dataset
