import numpy as np

arr = np.arange(10)

# sums the entire array together
np.sum(arr)  # 45
# equivalent to above
np.add.reduce(arr)  # 45

# statistical functions
np.mean(arr)  # 4.5
np.median(arr)  # 4.5
np.max(arr)  # 9
np.min(arr)  # 0
