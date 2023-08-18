import numpy as np

arr = np.array([1, 2, 3, 4])

# vectorized operations
# these operate on every element in the array
# no map + lambda or comprehension needed
print(arr + 1)  # [2, 3, 4, 5]

# multi-dimensional array
arr = np.array([[0, 1, 2, 3], [10, 11, 12, 13]])

# index into 2nd row, 2nd column
print(arr[1, 1])  # 11
