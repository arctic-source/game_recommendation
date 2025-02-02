from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt

from src.back_end.data_processing.helpers.load_dataset import load_dataset
from src.back_end.data_processing.transformers.to_pandas import ToPandas

dataset_raw = load_dataset()
processing_pipeline = Pipeline([
    ('to_pandas', ToPandas())
])
dataset = processing_pipeline.fit_transform(dataset_raw)

n_bins = 5000
fig_size = (13, 8)
style = 'fivethirtyeight'

# outlook
plt.figure(figsize=fig_size)
plt.style.use(style)
plt.hist(dataset['total_overall_reviews'], bins=n_bins)
plt.xlim([0, 100000])
# plt.ylim([0, 17000])
plt.title('Total number of reviews (outlook)')
plt.xlabel('Number of reviews')
plt.ylabel('Frequency')
plt.tight_layout()
plt.plot()

# zoom-in
plt.figure(figsize=fig_size)
plt.style.use(style)
plt.hist(dataset['total_overall_reviews'], bins=n_bins)
plt.xlim([0, 100000])
plt.ylim([0, 650])
plt.title('Total number of reviews (zoom-in)')
plt.xlabel('Number of reviews')
plt.ylabel('Frequency')
plt.tight_layout()
plt.plot()

plt.show()
