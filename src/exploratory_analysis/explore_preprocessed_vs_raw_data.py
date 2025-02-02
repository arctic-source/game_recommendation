from sklearn.pipeline import Pipeline

from src.back_end.data_processing.helpers.load_dataset import load_dataset
from src.back_end.data_processing.transformers.date_to_numeric import DateToNumeric
from src.back_end.data_processing.transformers.impute_dates import ImputeDates
from src.back_end.data_processing.transformers.impute_manual import ImputeManually
from src.back_end.data_processing.transformers.parse_dates import ParseDates
from src.back_end.data_processing.transformers.remove_nan import RemoveNan
from src.back_end.data_processing.transformers.remove_slashes import RemoveSlashes
from src.back_end.data_processing.transformers.to_pandas import ToPandas

suppress_output = False
dataset_raw = load_dataset()

# dataset 1 - no dropping na values
preprocessing_pipeline = Pipeline([
    ('to_pandas', ToPandas()),
    ('remove_slashes', RemoveSlashes()),
    ('manually_imputate_popular_games', ImputeManually())
])
dataset1 = preprocessing_pipeline.fit_transform(dataset_raw)

# dataset 2 - drop na values (and empty lists, ...)
preprocessing_pipeline = Pipeline([
    ('to_pandas', ToPandas()),
    ('remove_slashes', RemoveSlashes()),
    ('manually_imputate_popular_games', ImputeManually()),
    ('remove_nans', RemoveNan(
        keep_nans_in_columns=['nominal_overall_reviews', 'nominal_recent_reviews', 'total_recent_reviews',
                              'positive_recent_reviews'],
        suppress_output=False)),
    ('impute_dates', ImputeDates()),
    ('parse_dates', ParseDates()),
    ('date_to_numeric', DateToNumeric())
])
dataset2 = preprocessing_pipeline.fit_transform(dataset_raw)

user_defined_tags1 = dataset1['app_tags'].explode().unique()
user_defined_tags2 = dataset2['app_tags'].explode().unique()

genres1 = dataset1['genres'].explode().unique()
genres2 = dataset2['genres'].explode().unique()

developers1 = dataset1['developers'].explode().unique()
developers2 = dataset2['developers'].explode().unique()

publishers1 = dataset1['publishers'].explode().unique()
publishers2 = dataset2['publishers'].explode().unique()

print(f'\nNumber of developers - raw data: {len(developers1)}')
print(f'\nNumber of developers - preprocessed data: {len(developers2)}')

print(f'\nNumber of publishers - raw data: {len(publishers1)}')
print(f'\nNumber of publishers - preprocessed data: {len(publishers2)}')

print(f'\nUser defined tags - raw data ({len(user_defined_tags1)})')
print(user_defined_tags1)
print(f'\nUser defined tags - preprocessed data ({len(user_defined_tags2)})')
print(user_defined_tags2)

print(f'\nGenres - raw data ({len(genres1)})')
print(genres1)
print(f'\nGenres - preprocessed data ({len(genres2)})')
print(genres2)

print('\nRaw data characteristics:')
print(dataset1.describe().applymap('{:,.1f}'.format).to_string())
print('\nPreprocessed data characteristics:')
print(dataset2.describe().applymap('{:,.1f}'.format).to_string())
