from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class CommonSimilarity(BaseEstimator, TransformerMixin):
    def __init__(self, numerical_weight, categorical_weight):
        self.numerical_weight = numerical_weight
        self.categorical_weight = categorical_weight

    def fit(self, dataset, y=None):
        return self
    def transform(self, dataset, y=None):
        print('Calculating common similarity...')
        dataset['com_similarity'] = (self.numerical_weight * dataset['num_similarity'] + self.categorical_weight * dataset['cat_similarity'])/2
        return dataset