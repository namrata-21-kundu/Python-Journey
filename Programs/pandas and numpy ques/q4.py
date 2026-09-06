'''
Question:
Create a NumPy array containing numbers from 10 to 50 with a step of 5. Then display:

The array
Number of elements
Shape
Data type
'''

import numpy as np
arr = np.arange(10,51,5)
print(arr)
print(arr.size)
print(arr.shape)
print(arr.dtype)
