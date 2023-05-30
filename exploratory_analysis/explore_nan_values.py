from sklearn.pipeline import Pipeline

from data_processing.helpers.columns_that_contain_lists import columns_that_contain_lists
from data_processing.helpers.load_dataset import load_dataset
from data_processing.transformers.ImputeManually import ImputeManually
from data_processing.transformers.RemoveNan import RemoveNan
from data_processing.transformers.RemoveSlashes import RemoveSlashes
from data_processing.transformers.ToPandas import ToPandas

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
])
dataset2 = preprocessing_pipeline.fit_transform(dataset_raw)

# dataset 3 - data that was dropped by data cleaning
columns_with_lists = columns_that_contain_lists(dataset1)
# convert to string in order to calculate data that was dropped (need to have hashable type but some data are lists)
for column in columns_with_lists:
    dataset1[column] = dataset1[column].apply(lambda x: str(x))
    dataset2[column] = dataset2[column].apply(lambda x: str(x))
dataset3 = dataset1.merge(dataset2, how='outer', indicator=True)
dataset3 = dataset3[dataset3['_merge'] == 'left_only']
dataset3 = dataset3.drop(columns=['_merge'])
for column in columns_with_lists:
    dataset1[column] = dataset1[column].apply(lambda x: eval(x))
    dataset2[column] = dataset2[column].apply(lambda x: eval(x))
    dataset3[column] = dataset3[column].apply(lambda x: eval(x))

# nans_exist = check_if_nans_exist(dataset, suppress_output=False)
# mask = dataset.isna().any(axis=1)
# dataset_with_nan = dataset[mask]
dataset_with_nan_sorted_by_popularity = dataset3.sort_values(by='total_overall_reviews', ascending=False)

# List examples of games with nan values (most popular games by number of reviews)
head = dataset_with_nan_sorted_by_popularity.head(n=30)
print('Most popular games that have nan values:')
print(head.to_string())