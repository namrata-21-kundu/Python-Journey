'''
Question:
Generate an array of 10 random integers between 1 and 100 using NumPy.

Find:

Maximum
Minimum
Mean
Sum
'''

import numpy as np

arr = np.random.randint(1,101,10)

print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.sum(arr))