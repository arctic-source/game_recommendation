import pandas as pd
from sklearn.pipeline import Pipeline

from src.back_end.data_processing.helpers.load_dataset import load_dataset
from src.back_end.data_processing.transformers.date_to_numeric import DateToNumeric
from src.back_end.data_processing.transformers.impute_dates import ImputeDates
from src.back_end.data_processing.transformers.impute_manual import ImputeManually
from src.back_end.data_processing.transformers.parse_dates import ParseDates
from src.back_end.data_processing.transformers.remove_nan import RemoveNan
from src.back_end.data_processing.transformers.remove_slashes import RemoveSlashes
from src.back_end.data_processing.transformers.to_pandas import ToPandas

dataset = load_dataset()
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
dataset = preprocessing_pipeline.fit_transform(dataset)


num_of_most_frequent_words_in_descriptions = 40
most_frequent_words = pd.Series(
    ' '.join(dataset['game_description']).lower().split()
).value_counts()[:num_of_most_frequent_words_in_descriptions]

print('Most used words in game descriptions - raw data')
print(most_frequent_words)
