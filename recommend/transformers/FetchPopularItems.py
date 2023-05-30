from sklearn.base import BaseEstimator, TransformerMixin


class FetchPopularItems(BaseEstimator, TransformerMixin):
    def __init__(self, num_recommendations):
        self.num_recommendations = num_recommendations
    def fit(self, dataset, y=None):
        return self
    def transform(self, dataset, y=None):

        # get a number of recommendation based on highest similarity
        # however, do not recommend the most similar item because this item is the input item from user
        similarity_score = dataset['total_positive_reviews'].astype(float).sort_values(ascending=False)
        highest_similarity_score = similarity_score.iloc[0:self.num_recommendations+0]
        index_of_highest_similarity_score = list(highest_similarity_score.index)
        recommended_items = dataset.loc[index_of_highest_similarity_score]

        return recommended_items