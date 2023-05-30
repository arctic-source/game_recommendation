from sklearn.base import BaseEstimator, TransformerMixin


class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns:list):
        self.columns = columns
    def fit(self, dataset, y=None):
        return self
    def transform(self, dataset, y=None):
        print('Dropping columns...')
        dataset = dataset.drop(columns=self.columns)
        return dataset
