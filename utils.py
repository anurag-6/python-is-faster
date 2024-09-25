import time
from functools import wraps

fastest_func = None
fastest_time = float('inf')
fastest_args = None

def watch_process_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global fastest_func, fastest_time, fastest_args
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        elapsed_time = end - start

        if elapsed_time < fastest_time:
            fastest_func = func.__name__
            fastest_time = elapsed_time
            fastest_args = f"with args{args} and kwargs {kwargs}"

        print(f"Total time taken to execute {func.__name__} : {elapsed_time:.5f} seconds")
        return f"Fastest test case was : {fastest_func} {fastest_args},  took {fastest_time}"
    return wrapper