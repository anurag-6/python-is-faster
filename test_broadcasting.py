import numpy as np
from utils import watch_process_time

# Vanilla
a = range(50000000)
b = 5

@watch_process_time
def test_vanilla_way():
    c = [x * b for x in a]
    return c

# NumPy
a = np.array(range(5000000))
b = 5

@watch_process_time
def test_numpy_way():
    c = a * b
    return c

if __name__ == '__main__':
    res1 = test_numpy_way()
    res2 = test_vanilla_way()
    print(res2)