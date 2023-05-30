from sklearn.base import BaseEstimator, TransformerMixin

from recommend.similarity_measures.cos_similarity.cos_similarity import add_cos_similarity_column


class CosSimilarity(BaseEstimator, TransformerMixin):
    def __init__(self, instance, similarity_name):
        self.instance = instance
        self.similarity_name = similarity_name
    def fit(self, dataset, y=None):
        return self
    def transform(self, dataset, y=None):
        instance = self.instance[dataset.columns]
        dataset_with_similarity = add_cos_similarity_column(instance, dataset, self.similarity_name)
        return dataset_with_similarity