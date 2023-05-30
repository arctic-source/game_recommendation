from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

from data_processing.helpers.placeholders import CATEGORICAL_DATA, COLUMNS_TO_DROP, \
    COLUMNS_TO_ONE_HOT_ENCODE
from data_processing.helpers.load_dataset import load_dataset
from data_processing.transformers.CommonSimilarity import CommonSimilarity
from data_processing.transformers.DateToNumeric import DateToNumeric
from data_processing.transformers.DropColumns import DropColumns
from data_processing.transformers.ImputeDates import ImputeDates
from data_processing.transformers.ImputeManually import ImputeManually
from data_processing.transformers.OneHotEncode import OneHotEncode
from data_processing.transformers.ParseDates import ParseDates
from data_processing.transformers.RemoveNan import RemoveNan
from data_processing.transformers.RemoveSlashes import RemoveSlashes
from data_processing.transformers.RemoveTrademarkSymbols import RemoveTrademarkSymbols
from data_processing.transformers.ToPandas import ToPandas
from recommend.transformers.CosSimilarity import CosSimilarity
from recommend.transformers.FetchSimilarItems import FetchSimilarItems


def preprocess():
    """
    Preprocesses raw Steam games dataset.

    This function loads the raw dataset, applies a pipeline of preprocessing steps,
    and returns a clean pandas dataframe. The preprocessing steps include conversion
    to pandas, removal of trademark symbols, manual imputation, and removal of NaN
    values, excluding certain columns (these columns will be dropped later, no need
    to drop instances where there are NaN values in these columns).

    Pipeline steps:
    1. ToPandas: Converts the dataset to pandas dataframe.
    2. RemoveTrademarkSymbols: Removes trademark symbols from the dataset.
    3. ImputeManually: Manually imputes most popular game titles to prevent data loss due to NaN values.
    4. RemoveNan: Removes NaN values from the dataset except in specified columns.

    Returns:
    DataFrame: A clean and preprocessed dataframe ready for further processing.
    """

    print('Preprocessing ...')
    dataset_raw = load_dataset()

    columns_to_keep_nans_in = ['nominal_overall_reviews', 'nominal_recent_reviews', 'total_recent_reviews', 'positive_recent_reviews']


    preprocessing_pipeline = Pipeline([
        ('to_pandas', ToPandas()),
        # ('remove_slashes', RemoveSlashes()),
        ('remove_tm_symbols', RemoveTrademarkSymbols()),
        ('manually_impute_popular_games', ImputeManually()), # manually impute in order not to lose most popular game titles because of nan values present
        ('remove_nans', RemoveNan(keep_nans_in_columns=columns_to_keep_nans_in, suppress_output=True))
    ])
    dataset = preprocessing_pipeline.fit_transform(dataset_raw)
    print('Preprocessing: Done.\n')
    return dataset

def process(dataset_preprocessed):
    """
    Processes a preprocessed Steam game dataset for recommendation.

    This function takes a preprocessed pandas dataframe, applies a pipeline of
    processing steps, and returns a dataframe ready for similarity calculation
    for recommendations. The processing steps include imputation of day of the
    month, parsing dates, date conversion to numerical data, one hot encoding
    of categorical data, dropping unnecessary columns, and scaling.

    Parameters:
    dataset_preprocessed (DataFrame): Preprocessed dataframe ready for processing.

    Pipeline steps:
    1. ImputeDates: Imputes the day as the first of the month if day information is missing.
    2. ParseDates: Parses date features to a standard date format.
    3. DateToNumeric: Converts date features to numerical features.
    4. OneHotEncode: One hot encoding for categorical data (specified by COLUMNS_TO_ONE_HOT_ENCODE).
    5. DropColumns: Drops columns that are not necessary for recommendation.
    6. Scaler: Scales all numerical data to an interval of [0, 1] using RobustScaler (MinMaxScaler and StandardScaler are alternatives).
    7. ToPandas: Converts the numpy array back to a pandas dataframe with the original columns and index.

    Returns:
    DataFrame: A processed pandas dataframe ready for calculating similarities for recommendations.
    """
    print('Processing ...')
    columns_to_drop = COLUMNS_TO_DROP
    columns_to_drop.extend(CATEGORICAL_DATA)

    columns_for_similarity_calculation = ['price_eur', 'release_date', 'steam_rating', 'total_overall_reviews', 'positive_overall_reviews']
    columns_to_place_back = list(dataset_preprocessed.columns)
    for column in columns_to_drop:
        if column in columns_to_place_back:
            columns_to_place_back.remove(column)
    index_to_place_back = dataset_preprocessed.index


    # move the 'title' column to the end of the column list because such shuffled is the dataframe after standard scaling
    columns_to_place_back.append(columns_to_place_back[0])
    columns_to_place_back.pop(0)
    # get column names after one hot encoding
    _place_back_cols = list(dataset_preprocessed['app_tags'].explode().unique())
    _place_back_cols = [f'app_tags_{i}' for i in _place_back_cols]
    _place_back_cols.sort()
    columns_to_place_back.extend(_place_back_cols)


    processing_pipeline = Pipeline([
        ('impute_dates', ImputeDates()),
        ('parse_dates', ParseDates()),
        ('date_to_numeric', DateToNumeric()),
        ('one_hot_encode', OneHotEncode(columns=COLUMNS_TO_ONE_HOT_ENCODE)),
        ('drop_columns', DropColumns(columns=columns_to_drop)),
        ('scale', ColumnTransformer([
            # ('scale', MinMaxScaler(), columns_for_similarity_calculation)
            # ('scale', StandardScaler(), columns_for_similarity_calculation)
            ('scale', RobustScaler(), columns_for_similarity_calculation)
        ], remainder='passthrough')),
        ('to_pandas', ToPandas(columns=columns_to_place_back, index=index_to_place_back))
    ])
    dataset = processing_pipeline.fit_transform(dataset_preprocessed)
    print('Processing: Done.\n')
    return dataset


