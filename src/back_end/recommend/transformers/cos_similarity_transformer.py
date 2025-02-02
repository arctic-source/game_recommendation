from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
from src.back_end.recommend.similarity_measures.cos_similarity import add_cos_similarity_column


class CosineSimilarity(BaseEstimator, TransformerMixin):
    """
    A transformer that computes cosine similarity between an instance and a dataset.

    This transformer calculates the cosine similarity between a given `instance` and all rows
    in the dataset, adding a new column with similarity scores.

    Attributes:
        instance (pd.Series or pd.DataFrame): The reference instance to compare against.
        similarity_name (str): The name of the new similarity column to be added.

    Methods:
        fit(dataset, y=None):
            Returns the transformer instance (no fitting required).

        transform(dataset, y=None):
            Computes cosine similarity and adds it as a new column.
    """

    def __init__(self, instance: pd.Series, similarity_name: str):
        """
        Initializes the CosineSimilarity transformer.

        Args:
            instance (pd.Series or pd.DataFrame): The reference instance to compute similarity against.
            similarity_name (str): The name of the new similarity column.
        """
        self.instance = instance
        self.similarity_name = similarity_name

    def fit(self, dataset: pd.DataFrame, y=None):
        """
        Fit method for scikit-learn compatibility. Does nothing and returns self.

        Args:
            dataset (pd.DataFrame): The input dataset (ignored).
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            CosineSimilarity: Returns self.
        """
        return self

    def transform(self, dataset: pd.DataFrame, y=None) -> pd.DataFrame:
        """
        Computes cosine similarity between the `instance` and each row in the dataset.

        The similarity score is added as a new column named `similarity_name`.

        Args:
            dataset (pd.DataFrame): The input dataset.
            y: Unused parameter for compatibility with scikit-learn pipelines.

        Returns:
            pd.DataFrame: The dataset with the additional similarity column.
        """

        # extract relevant columns from the instance to ensure matching column names
        instance_filtered = self.instance[dataset.columns]

        # compute cosine similarity and add the new similarity column
        dataset_with_similarity = add_cos_similarity_column(instance_filtered, dataset, self.similarity_name)

        return dataset_with_similarity
