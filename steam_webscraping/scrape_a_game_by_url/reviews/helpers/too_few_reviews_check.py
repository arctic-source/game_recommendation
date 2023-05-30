def too_few_reviews_check(nominal_reviews):
    # Check if there are too few reviews to extract a meaningful nominal review
    if nominal_reviews is not None:
        if nominal_reviews[0] is not None:
            if nominal_reviews[0].isdigit():
                return True
    if nominal_reviews is None:
        return True
    else:
        if nominal_reviews[0] is None:
            return True
    return False
