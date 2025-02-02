import numpy as np


def duplicates_exist(input_list: list) -> bool:
    duplicates_exist = not np.unique(input_list).size == len(input_list)
    return duplicates_exist
