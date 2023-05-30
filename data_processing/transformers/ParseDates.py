from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class ParseDates(BaseEstimator, TransformerMixin):
    def fit(self, dataset, y=None):
        return self
    def transform(self, dataset, y=None):
        print('Parsing dates...')
        dataset['release_date'] = pd.to_datetime(dataset['release_date'], format='%d %b %Y')
        return dataset