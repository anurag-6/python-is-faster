import time
import numpy as np
from utils import watch_process_time

# Vanilla
arr = range(5000000)

@watch_process_time
def test_vanilla_way():
    filtered_arr = [x for x in arr if x > 2]

# NumPy
arr = np.array(range(5000000))

@watch_process_time
def test_numpy_way():
    mask = arr > 2
    filtered_arr = arr[mask]

if __name__ == '__main__':
    res1 = test_numpy_way()
    res2 = test_vanilla_way()
    print(res2)