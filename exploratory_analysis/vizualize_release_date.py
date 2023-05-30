from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt

from data_processing.helpers.load_dataset import load_dataset
from data_processing.transformers.DropColumns import DropColumns
from data_processing.transformers.ImputeDates import ImputeDates
from data_processing.transformers.ImputeManually import ImputeManually
from data_processing.transformers.ParseDates import ParseDates
from data_processing.transformers.RemoveNan import RemoveNan
from data_processing.transformers.RemoveSlashes import RemoveSlashes
from data_processing.transformers.ToPandas import ToPandas


dataset_raw = load_dataset()
preprocessing_pipeline = Pipeline([
    ('to_pandas', ToPandas()),
    ('remove_slashes', RemoveSlashes()),
    ('manually_imputate_popular_games', ImputeManually()),
    # manually impute in order not to lose huge game titles because of nan values present
    ('remove_nans', RemoveNan(
        keep_nans_in_columns=['nominal_overall_reviews', 'nominal_recent_reviews', 'total_recent_reviews',
                              'positive_recent_reviews'],
        suppress_output=False)),
    ('drop_columns', DropColumns(
        columns=['nominal_overall_reviews', 'nominal_recent_reviews', 'total_recent_reviews', 'positive_recent_reviews',
                 'steam_id', 'url']
    )),
    ('impute_dates', ImputeDates()),
    ('parse_dates', ParseDates())
])

dataset = preprocessing_pipeline.fit_transform(dataset_raw)

n_bins = 1000
fig_size = (13, 8)
style = 'fivethirtyeight'

# outlook
plt.figure(figsize=fig_size)
plt.style.use(style)
plt.hist(dataset['release_date'], bins=n_bins)
# plt.xlim([0, 100000])
# plt.ylim([0, 17000])
plt.title('Release dates (outlook)')
plt.xlabel('Date')
plt.ylabel('Frequency')
plt.tight_layout()
plt.plot()

# # zoom-in
# plt.figure(figsize=fig_size)
# plt.style.use(style)
# plt.hist(dataset['total_overall_reviews'], bins=n_bins)
# plt.xlim([0, 100000])
# plt.ylim([0, 650])
# plt.title('Total number of reviews (zoom-in)')
# plt.xlabel('Number of reviews')
# plt.ylabel('Frequency')
# plt.tight_layout()
# plt.plot()

plt.show()

