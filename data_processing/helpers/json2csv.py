import os

from data_processing.helpers.load_dataset import load_dataset
from data_processing.transformers.ToPandas import to_pandas


def json2csv():
    """Load steam dataset from thousands of json files, convert the dataset to pandas dataframe, save the dataset as csv."""

    project_path = os.path.dirname(os.getcwd())
    csv_path = os.path.join('steam_data', 'steam_game_data')
    csv_file_name = 'steam_dataset.csv'
    save_path = os.path.join(project_path, csv_path, csv_file_name)

    dataset_raw = load_dataset()
    dataset_pandas = to_pandas(dataset_raw)
    dataset_pandas.to_csv(save_path, sep=';', index=False)

json2csv()