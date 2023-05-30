from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class RemoveTrademarkSymbols(BaseEstimator, TransformerMixin):
    def fit(self, dataset: pd.DataFrame, y=None):
        return self
    def transform(self, dataset: pd.DataFrame, y=None):
        print('Removing TM symbols ...')
        unwanted_characters = ['™', '®']
        for character in unwanted_characters:
            dataset['title'] = dataset['title'].str.replace(character, '')
        return dataset

