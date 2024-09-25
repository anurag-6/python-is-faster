import numpy as np
from utils import watch_process_time

# Vanilla
arr = range(5000000)

@watch_process_time
def test_vanilla_way():
   sum_ = sum(arr)

# NumPy
arr = np.array(range(5000000))

@watch_process_time
def test_numpy_way():
    sum = arr.sum()

if __name__ == '__main__':
    res1 = test_numpy_way()
    res2 = test_vanilla_way()

