import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
def add_cos_similarity_column(instance, dataset, similarity_name):
    # calculates the cosine similarity of instance with every other instance in the dataset
    dataset_numpy = dataset.to_numpy()
    instance_numpy = instance.to_numpy()
    similarity_array = cosine_similarity(instance_numpy, dataset_numpy)
    if similarity_name != '':
        new_column_name = f'{similarity_name}_similarity'
    else:
        new_column_name = 'similarity'
    dataset[new_column_name] = similarity_array.transpose()
    return dataset





def cos_similarity_non_optimized(array1, array2):
    return np.dot(array1, array2) / (np.linalg.norm(array1) * np.linalg.norm(array2))
