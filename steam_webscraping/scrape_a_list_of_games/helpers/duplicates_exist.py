import numpy as np

def duplicates_exist(input: list) -> bool:
    duplicates_exist = not np.unique(input).size == len(input)
    return duplicates_exist