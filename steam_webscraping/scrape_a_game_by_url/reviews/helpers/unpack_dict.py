def unpack_dict(reviews: dict):
    nominal = reviews['nominal_reviews']
    total = reviews['total_reviews']
    positive = reviews['positive_reviews']
    positive_percentage = reviews['positive_reviews_percentage']

    return nominal, total, positive, positive_percentage
