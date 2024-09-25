import numpy as np
import time
# --------------------------- 1. Vectorized Operations---------------------------------

"""
Why this way?
    Vectorized operations allow you to perform computations on entire arrays without explicit loops,
    resulting in faster and more efficient code.

What was the general (vanilla) way?
    In vanilla Python, you'd typically use loops (like for loops) to iterate over lists and perform element-wise operations.

What is the advantage of this way?
    Speed: Vectorized operations are implemented in low-level languages (like C), making them much faster than Python loops.
    Conciseness: Your code becomes shorter and more readable.
    Less Error-Prone: Fewer lines of code reduce the chance of bugs.

When to consider?
    Use vectorized operations when performing element-wise computations on arrays or large datasets.

What is Vectorization?
    NumPy arrays can only have a single data type and the data is stored in a continuous block of memory. 
    By utilizing this, NumPy performs operations on these arrays by delegating them to optimized pre-compiled C code,
    which improves performance.
Ref:
    https://medium.com/pythoneers/vectorization-in-python-an-alternative-to-python-loops-2728d6d7cd3e
"""

# Vanilla Python way
a = [1, 2, 3]
b = [4, 5, 6]
c = []
for i in range(len(a)):
    c.append(a[i] + b[i])
print(c)  # Output: [5, 7, 9]


# NumPy way: note raises ValueError if len doesnt match
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b  # Vectorized addition
print(c)  # Output: [5 7 9]


# --------------------------- 2. Broadcasting ---------------------------------


"""
Why this way?
    Broadcasting allows you to perform arithmetic operations on arrays of different shapes, simplifying code and improving performance.

What was the general (vanilla) way?
    In vanilla Python, you might need to use nested loops or manually adjust data structures to match dimensions.

What is the advantage of this way?
    Simplifies Code: Eliminates the need for loops to match array dimensions.
Efficiency: Performs operations at C-speed without extra memory overhead.
Flexibility: Easily applies operations between arrays of different shapes.
When to consider?
    Use broadcasting when you need to perform operations between arrays of different shapes or when applying a scalar operation to an array.
"""

# vanilla
# Multiplying a list by a scalar
a = [i for i in range(50000)]
b = 5
c = [x * b for x in a]
print(c)  # Output: [5, 10, 15]

# numpy
# Broadcasting scalar multiplication
a = np.array([i for i in range(50000)])
b = 5
c = a * b  # Broadcasting applies multiplication to each element
print(c)  # Output: [ 5 10 15]


# --------------------------- 3. Efficient Array Slicing ---------------------------------

"""
Why this way?
    NumPy array slicing allows you to access subarrays without copying data, leading to faster operations and lower memory usage.

What was the general (vanilla) way?
    In vanilla Python, slicing lists creates new lists, which can be inefficient for large datasets.

What is the advantage of this way?
    Performance: Faster access to subarrays without data copying.
    Memory Efficiency: Reduces memory footprint by referencing data instead of copying.
    Ease of Use: Simplifies code when working with subarrays.
When to consider?
    Use efficient slicing when you need to work with parts of large arrays without the overhead of copying data.
"""

# Slicing a list (creates a new list)
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sub_arr = [row[:2] for row in arr[:2]]
print(sub_arr)  # Output: [[1, 2], [4, 5]]


# Efficient slicing without data copying
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
sub_arr = arr[:2, :2]
print(sub_arr)  # Output: [[1 2]
                #          [4 5]]


# --------------------------- 4. Boolean Masking ---------------------------------

"""
Why this way?
    Boolean masking allows you to filter arrays based on conditions without explicit loops, making code more efficient and readable.

What was the general (vanilla) way?
    In vanilla Python, you'd use list comprehensions or loops with conditional statements to filter data.

What is the advantage of this way?
    Speed: Faster than loops or list comprehensions for large datasets.
    Readability: More concise and expressive code.
    Flexibility: Easily combine multiple conditions.
When to consider?
    Use boolean masking when you need to filter or select elements from an array based on conditions
"""


# Filtering a list based on a condition
arr = [1, 2, 3, 4, 5]
filtered_arr = [x for x in arr if x > 2]
print(filtered_arr)  # Output: [3, 4, 5]


# Boolean masking
arr = np.array([1, 2, 3, 4, 5])
mask = arr > 2
filtered_arr = arr[mask]
print(filtered_arr)  # Output: [3 4 5]


# --------------------------- 5. Aggregation Functions ---------------------------------
"""
Why this way?
    NumPy's aggregation functions compute summaries (like sum, mean) over arrays efficiently, especially for large datasets.

What was the general (vanilla) way?
    Using built-in Python functions like sum() or third-party libraries, which are slower for large lists.

What is the advantage of this way?
    Performance: NumPy functions are optimized and faster.
    Convenience: Provides a wide range of aggregation functions.
    Axis Control: Easily aggregate along specific dimensions in multi-dimensional arrays.
When to consider?
    Use NumPy's aggregation functions when working with numerical data that requires summary statistics.
"""

# Summing elements in a list
arr = [1, 2, 3, 4, 5]
total_sum = sum(arr)
print(total_sum)  # Output: 15


# Using NumPy's sum function
arr = np.array([1, 2, 3, 4, 5])
total_sum = np.sum(arr)
print(total_sum)  # Output: 15


# top methods

# Sum of elements in an array
sum_of_arr = np.sum(arr)

# Mean (average) of elements in an array
mean_of_arr = np.mean(arr)

# Median of elements in an array
median_of_arr = np.median(arr)

# Standard deviation of elements in an array
std_of_arr = np.std(arr)

# Variance of elements in an array
var_of_arr = np.var(arr)

# Maximum value in an array
max_value = np.max(arr)

# Minimum value in an array
min_value = np.min(arr)

# Index of the minimum value in an array
min_index = np.argmin(arr)

# Index of the maximum value in an array
max_index = np.argmax(arr)

# Product of elements in an array
product_of_arr = np.prod(arr)