from sklearn.base import BaseEstimator, TransformerMixin


class ProcessSimilarItems(BaseEstimator, TransformerMixin):
    def fit(self, dataset, y=None):
        return self
    def transform(self, dataset, y=None):
        titles = dataset['titles']
        return titles