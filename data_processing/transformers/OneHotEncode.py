from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class OneHotEncode(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns_to_one_hot_encode = columns
    def fit(self, dataset: pd.DataFrame, y=None):
        return self
    def transform(self, dataset: pd.DataFrame, y=None):
        print('One hot encoding...')
        for column in self.columns_to_one_hot_encode:
            one_hot_encoded = pd.get_dummies(dataset['app_tags'].explode(), prefix=column, prefix_sep='_', columns=[column])
            # Sum the one-hot encoded columns by index (grouping by the original DataFrame index)
            one_hot_encoded_grouped = one_hot_encoded.groupby(level=0).sum()
            dataset = pd.concat([dataset, one_hot_encoded_grouped], axis=1)

            l2 = list(dataset['app_tags'].explode().unique())
            l1 = list(dataset.columns[18:])
        return dataset

