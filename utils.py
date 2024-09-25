import time
from functools import wraps
from colorama import init, Fore, Style

init()

fastest_func = None
slowest_time = None
fastest_time = float('inf')
fastest_args = None
call_time = 0

def watch_process_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global fastest_func, fastest_time, fastest_args, call_time, slowest_time
        start = time.perf_counter()
        call_time +=1
        func(*args, **kwargs)
        end = time.perf_counter()
        elapsed_time = end - start

        if elapsed_time < fastest_time:
            fastest_func = func.__name__
            fastest_time = elapsed_time
            fastest_args = f"with args{args} and kwargs {kwargs}"

        if call_time > 0:
            if elapsed_time > fastest_time:
                slowest_time = elapsed_time

        print(f"{Fore.GREEN}Total time taken to execute {func.__name__} : {elapsed_time:.5f} seconds{Style.RESET_ALL}")
        if call_time > 1:
            print(f"{Fore.BLUE}Fastest test case was : {fastest_func} {fastest_args},  took {fastest_time}{Style.RESET_ALL}")
            x_faster = slowest_time / fastest_time
            print(f"{Fore.RED}That was {x_faster} X Faster!!!!!{Style.RESET_ALL}")
            return f"Fastest test case was : {fastest_func} {fastest_args},  took {fastest_time}"
    return wrapper