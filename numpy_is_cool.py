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

#  add two arrays
np.concatenate((a, b))

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


# --------------------------- 6. NumPy's Random Module ---------------------------------

"""
Why this way?
    NumPy's random module efficiently generates random numbers and arrays, which is faster and more powerful than Python's built-in random module.

What was the general (vanilla) way?
    Using Python's random module to generate random numbers, which is slower for large-scale random data generation.

What is the advantage of this way?
    Performance: Faster random number generation for large arrays.
    Functionality: Offers more distributions and functions.
    Array Support: Directly generates arrays of random numbers.
When to consider?
    Use NumPy's random module when you need to generate large amounts of random data or require advanced random distributions.

"""

import random

# Generating 1000 random integers
random_numbers = [random.randint(0, 100) for _ in range(1000)]


# Generating 1000 random integers efficiently
import numpy as np

# Generating 1000 random integers efficiently
random_numbers = np.random.randint(0, 101, size=1000)


# --------------------------- 7. Efficient Memory Usage ---------------------------------

"""
Why this way?
    NumPy allows you to specify data types (like np.float32, np.int16), reducing memory usage for large datasets.

What was the general (vanilla) way?
    Vanilla Python's data types are more memory-intensive and less flexible in specifying precision.

What is the advantage of this way?
    Memory Efficiency: Lower memory footprint for large arrays.
    Performance: Reduced memory usage can lead to performance gains.
    Precision Control: Ability to specify the exact data type needed.
When to consider?
    Use efficient data types when working with large datasets where memory usage is a concern.
"""

# Python integers (no direct way to specify bit size)
arr = [1, 2, 3]

# Specifying data type to reduce memory usage
arr = np.array([1, 2, 3], dtype=np.int16)
print(arr.dtype)  # Output: int16


# --------------------------- 8. Reshaping Arrays ---------------------------------
"""
Why this way?
    NumPy allows you to reshape arrays efficiently without copying data, facilitating data manipulation for computations.

What was the general (vanilla) way?
    In vanilla Python, you'd need to create new lists or use nested loops to rearrange data structures.

What is the advantage of this way?
    Efficiency: Reshapes without copying data.
    Flexibility: Easily change array dimensions.
    Convenience: Simplifies code when manipulating data shapes.
When to consider?
    Use reshaping when preparing data for algorithms that require specific input shapes.
"""


# Reshaping data manually
arr = [0, 1, 2, 3, 4, 5]
reshaped = [arr[i:i+2] for i in range(0, len(arr), 2)]
print(reshaped)  # Output: [[0, 1], [2, 3], [4, 5]]


# Reshaping using NumPy
arr = np.arange(6)
reshaped = arr.reshape(3, 2)
print(reshaped)  # Output: [[0 1]
                 #          [2 3]
                 #          [4 5]]

# --------------------------- 9.  Advanced Indexing ---------------------------------
"""
Why this way?
    Advanced indexing in NumPy allows you to access elements using arrays of indices,
    enabling complex data retrieval without loops.

What was the general (vanilla) way?
    Using loops or list comprehensions to access specific elements based on their indices.

What is the advantage of this way?
    Speed: Faster data access for large arrays.
    Simplicity: Reduces code complexity.
    Power: Can handle multi-dimensional arrays with ease.
When to consider?
    Use advanced indexing when you need to extract or modify specific elements in an array based on index arrays.
"""

# Accessing elements using indices
arr = [10, 20, 30, 40]
indices = [1, 3]
selected_elements = [arr[i] for i in indices]
print(selected_elements)  # Output: [20, 40]

# Advanced indexing in NumPy
arr = np.array([10, 20, 30, 40])
indices = [1, 3]
selected_elements = arr[indices]
print(selected_elements)  # Output: [20 40]


