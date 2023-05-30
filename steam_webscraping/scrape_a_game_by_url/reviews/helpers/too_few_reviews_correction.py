def too_few_recent_reviews_correction(reviews: dict):
    reviews['nominal_recent_reviews'] = None
    return reviews

def too_few_overall_reviews_correction(reviews: dict):
    try:
        total_num_reviews = reviews['nominal_overall_reviews'].split(' ')
        total_num_reviews = total_num_reviews[0]
        total_num_reviews = int(total_num_reviews)
        reviews['total_overall_reviews'] = total_num_reviews
        reviews['nominal_overall_reviews'] = None
    except:
        reviews['nominal_overall_reviews'] = None
    return reviews

