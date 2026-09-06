'''
Question:
Create a figure of size 10 × 6 containing two subplots arranged vertically.

First subplot: line graph of x and y1
Second subplot: line graph of x and y2

Given:

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 30, 40, 50]
y2 = [50, 40, 30, 20, 10]
'''

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 30, 40, 50]
y2 = [50, 40, 30, 20, 10]

fig, axes =  plt.subplots(2,1,figsize=(10,6))
axes[0].plot(x,y1)
axes[0].set_title("Increasing Values")

axes[1].plot(x, y2)
axes[1].set_title("Decreasing Values")


plt.tight_layout()
plt.show()