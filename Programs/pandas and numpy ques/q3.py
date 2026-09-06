'''
Question:
Create a NumPy array containing the following marks:

[78, 85, 92, 67, 88, 76, 95, 81, 69, 90]

Write a Python program to:

Display the array.
Find the maximum mark.
Find the minimum mark.
Calculate the average mark.
Calculate the total marks.
Find the standard deviation.
'''

import numpy as np
marks = np.array(
[78, 85, 92, 67, 88, 76, 95, 81, 69, 90])

print("Array:", marks)
print("Maximum: ", np.max(marks))
-=