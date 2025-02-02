from time import time


def measure_elapsed_time(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        runtime = end_time - start_time
        print(f"Function '{func.__name__}' executed in {runtime:.2f} seconds.")
        return result
    return wrapper
