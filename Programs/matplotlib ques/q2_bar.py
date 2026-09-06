'''
Question:
Using Matplotlib, create a bar graph for the following data:

subjects = ['Math', 'Science', 'English', 'Computer']
marks = [85, 78, 92, 88]

The graph should contain:

Title
X-axis label
Y-axis label
Different colors for the bars
Border around each bar
'''
import matplotlib.pyplot as plt

subjects = ['Math', 'Science', 'English', 'Computer']
marks = [85, 78, 92, 88]

colors = ['red', 'blue', 'green', 'orange']

plt.bar(subjects, marks, color = colors, edgecolor = 'black')

plt.title("Student marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()