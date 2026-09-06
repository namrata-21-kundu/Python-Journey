'''
Question:
Write a Python program using Matplotlib to create a line graph for the following data:

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

The graph should have:

A suitable title
X-axis label as "Days"
Y-axis label as "Sales"
A grid
A legend
'''
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x,y,label = 'Sales')

plt.title("Sales over days")
plt.xlabel("days")
plt.ylabel("Sales")

plt.grid()
plt.legend()

plt.show()  