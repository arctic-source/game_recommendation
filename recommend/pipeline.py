from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from data_processing.transformers.CommonSimilarity import CommonSimilarity
from data_processing.transformers.ToPandas import ToPandas
from recommend.transformers.CosSimilarity import CosSimilarity
from recommend.transformers.FetchSimilarItems import FetchSimilarItems


def recommend(instance, dataset_processed, dataset_preprocessed, num_recommendations):
    """
    Provides recommendations for a specific instance based on processed Steam game dataset.

    This function takes an instance from the dataset and calculates its similarity with other instances
    in the dataset, both numerical and categorical. It then returns a set number of items most similar
    to the given instance.

    Parameters:
    instance (Series): The instance for which recommendations are to be made.
    dataset_processed (DataFrame): The processed dataframe used to calculate similarities.
    dataset_preprocessed (DataFrame): The preprocessed dataframe to fetch recommendation details.
    num_recommendations (int): The number of recommendations to be returned.

    Pipeline steps:
    1. Similarity_preprocessor: Calculates cosine similarity for numerical and categorical columns.
    2. ToPandas1: Converts the numpy array to a pandas dataframe with similarity scores.
    3. CommonSimilarity: Calculates a common similarity score based on numerical and categorical similarity scores.
    4. ToPandas2: Converts the numpy array with common similarity scores back to a pandas dataframe.
    5. FetchSimilarItems: Fetches the required number of items most similar to the given instance.

    Returns:
    DataFrame: A dataframe with the recommended items, including their URL, title, and steam_id.
    """
    print('Recommending...')

    similarity_calc_numerical_columns = ['price_eur', 'release_date', 'steam_rating', 'total_overall_reviews',
                                          'positive_overall_reviews']
    similarity_calc_categorical_columns = [col for col in dataset_processed.columns if 'app_tags' in col]
    columns_to_place_back = similarity_calc_numerical_columns.copy()
    columns_to_place_back.append('num_similarity')
    columns_to_place_back.extend(similarity_calc_categorical_columns)
    columns_to_place_back.append('cat_similarity')
    columns_to_place_back.append('com_similarity')

    index_to_place_back = dataset_processed.index

    instance_index = instance.index
    instance = dataset_processed.loc[instance_index]

    recommendation_pipeline = Pipeline([
        ('similarity_preprocessor', ColumnTransformer(transformers=[
            ('num', CosSimilarity(instance, 'num'), similarity_calc_numerical_columns),
            ('cat', CosSimilarity(instance, 'cat'), similarity_calc_categorical_columns)
        ],
            remainder='passthrough')),
        ('to_pandas1', ToPandas(columns=columns_to_place_back, index=index_to_place_back)),
        ('common_similarity', CommonSimilarity(numerical_weight=1, categorical_weight=0.6)),
        ('to_pandas2', ToPandas(columns=columns_to_place_back, index=index_to_place_back)),
        ('fetch_similar_items', FetchSimilarItems(num_recommendations=num_recommendations))
    ])


    recommended_items = recommendation_pipeline.fit_transform(dataset_processed)
    recommended_items_index = recommended_items.index
    recommended_items['url'] = dataset_preprocessed.loc[recommended_items_index]['url']
    recommended_items['title'] = dataset_preprocessed.loc[recommended_items_index]['title']
    recommended_items['steam_id'] = dataset_preprocessed.loc[recommended_items_index]['steam_id']

    print('Recommending: Done.\n')
    return recommended_items