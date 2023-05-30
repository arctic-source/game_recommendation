from sklearn.base import BaseEstimator, TransformerMixin

from data_processing.helpers.manual_imputer import manual_imputer


class ImputeManually(BaseEstimator, TransformerMixin):
    def fit(self, dataset, y=None):
        return self
    def transform(self, dataset, y=None):
        print('Imputing...')
        dataset = manual_imputer(dataset)
        return dataset