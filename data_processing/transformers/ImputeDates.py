from sklearn.base import BaseEstimator, TransformerMixin


from data_processing.helpers.custom_date_imputer import custom_date_imputer


class ImputeDates(BaseEstimator, TransformerMixin):
    def fit(self, dataset, y=None):
        return self
    def transform(self, dataset, y=None):
        print('Imputing dates...')
        # if date is in format "Apr 2020", impute day of the month -> "1 Apr 2020"
        dataset['release_date'] = dataset['release_date'].apply(custom_date_imputer)
        return dataset