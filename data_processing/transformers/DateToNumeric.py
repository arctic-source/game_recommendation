from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class DateToNumeric(BaseEstimator, TransformerMixin):
    def fit(self, dataset, y=None):
        return self
    def transform(self, dataset, y=None):
        print('Transforming date to numeric format...')
        reference_year = '01 Jan 1970'
        reference_year = pd.to_datetime(reference_year, format='%d %b %Y')
        dataset['release_date'] = (dataset['release_date'] - reference_year).dt.days
        return dataset