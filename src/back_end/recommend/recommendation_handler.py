import pandas as pd

from src.back_end.placeholders import NUM_RECOMMENDATIONS, BLANK_THUMBNAIL_PATH
from src.back_end.recommend.pipeline import recommend
from src.back_end.steam_webscraping.scrape_game_thumbnail.fetch_game_thumbnail_path import fetch_game_thumbnail_path


def handle_recommend_action(user_input_text: str, dataset_processed: pd.DataFrame,
                            dataset_preprocessed: pd.DataFrame) -> dict:
    """
    Handles recommendation. Initializes game data from inputs, handles situation of empty game data, recommends similar
    games, collects and returns the results of the recommendation.
    Args:
        user_input_text (str): game title that user inputs into the line editor
        dataset_processed: dataset ready for similar game search
        dataset_preprocessed: dataset with NaNs handled, manual imputations etc.

    Returns:
        results (dict): titles, urls and paths to downloaded thumbnails of recommended games

    """

    # initialize empty game titles, urls, blank thumbnails
    titles = ['' for i in range(NUM_RECOMMENDATIONS)]
    urls = ['' for i in range(NUM_RECOMMENDATIONS)]
    thumbnail_paths = [BLANK_THUMBNAIL_PATH for i in range(NUM_RECOMMENDATIONS)]
    empty_results = {
        "titles": titles,
        "urls": urls,
        "thumbnail_paths": thumbnail_paths
    }

    # handle empty game data - can happen because of user or steam website
    if user_input_text is None:
        return empty_results
    elif user_input_text == '':
        return empty_results

    # check if desired game was scraped from web, handle case when not scraped
    titles_lowercase = dataset_processed['title'].str.lower().tolist()
    user_input_text_lowercase = user_input_text.lower()
    if user_input_text_lowercase not in titles_lowercase:
        return empty_results

    # get game instance from web scraped dataset that matches user input
    instance = dataset_processed.loc[dataset_processed['title'].str.lower() == user_input_text_lowercase]

    # get list of recommended titles similar to user input
    recommendations_dataframe = recommend(
        instance=instance,
        dataset_processed=dataset_processed,
        dataset_preprocessed=dataset_preprocessed,
        num_recommendations=NUM_RECOMMENDATIONS
    )
    titles = recommendations_dataframe['title'].tolist()

    # plot_recommendation_vectors(instance, dataset_processed, recommendations_dataframe, method='pca',
    #                             save_path='recommendation_visualization.png')

    # get urls of recommended games
    urls = dataset_preprocessed.loc[recommendations_dataframe.index]['url'].tolist()

    # game thumbnails of recommended games
    thumbnail_paths = []
    for url in urls:
        thumbnail_paths.append(fetch_game_thumbnail_path(steam_game_url=url))

    # fill in and return the results
    results = empty_results
    results["titles"] = titles
    results["urls"] = urls
    results["thumbnail_paths"] = thumbnail_paths
    return results
