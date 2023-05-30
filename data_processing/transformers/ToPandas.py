from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
from typing import Optional


def to_pandas(dataset_raw, columns, index):
    """ Convert a list to Pandas dataframe """
    dataset = pd.DataFrame(dataset_raw, columns=columns, index=index)
    return dataset

class ToPandas(BaseEstimator, TransformerMixin):
    def __init__(self, columns: Optional[list] = None, index: Optional[list] = None):
        self.columns = columns
        self.index = index

    def fit(self, dataset_raw, y=None):
        return self
    def transform(self, dataset_raw, y=None):
        print('Transforming to pandas...')
        dataset_pandas = to_pandas(dataset_raw, self.columns, self.index)
        return dataset_pandas

