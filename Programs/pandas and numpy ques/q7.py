'''
Question:
Given:

marks = np.array([45, 78, 92, 34, 67, 88, 56, 91, 40, 73])

Write a program to:

Display all marks greater than 70.
Display all marks less than 50.
Count how many students scored more than 70.
'''

import numpy as np
marks = np.array([45, 78, 92, 34, 67, 88, 56, 91, 40, 73])
print("marks greater than 70: ", marks[marks>70])
