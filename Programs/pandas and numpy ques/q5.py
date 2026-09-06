'''
Create a NumPy array containing numbers from 1 to 12. Reshape it into a 3 × 4 matrix and display the matrix.

Then display:

First row
Last column
Element at second row and third column
'''

import numpy as np
arr = np.arrange(1,13)
matrix = arr.reshape(3,4)

print("matrix: ", matrix)

print("first row: ", matrix[0])
print("last column: ", matrix[:, -1])

print("second row, third col: ", matrix[1,2])