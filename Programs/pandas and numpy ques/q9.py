'''
Question:
Create the following DataFrame:

Name	Age	Marks
Ayan	20	85
Riya	21	92
Rahul	19	67
Sneha	20	78
Arjun	22	95

Write a program to display:

Complete DataFrame
First 3 rows
Last 2 rows
Information about the DataFrame
Statistical summary

Using the DataFrame from Question 7:

Display only the Name column.
Display only the Marks column.
Find the average marks.
Find the highest marks.
Find the lowest marks.

Question:
Using the same DataFrame, display:

Students who scored more than 80.
Students whose age is 20.
Students who scored between 70 and 90.

Fast answer

To close (deactivate) a Python virtual environment, use:

deactivate

This works for most virtual environments, including:

venv
virtualenv

After running it, your shell prompt will no longer show the virtual environment name (e.g., (venv)), and you'll be back to your system's default Python.

If you're using Conda

Use:

conda deactivate
If deactivate doesn't work

Make sure the virtual environment is actually activated. If you simply opened the environment's folder without activating it, there's nothing to deactivate.

If you tell me which virtual environment you're using (venv, virtualenv, conda, pipenv, poetry, etc.) and your operating system, I can give the exact command.

Today 3:15 PM
1. Write a function that takes a list of numerical values and returns the minimum,
maximum, average, and sum.
2. Write a function that takes a list of class labels and returns a dictionary with the
count of each label. (labels = [&#39;spam&#39;, &#39;ham&#39;, &#39;spam&#39;, &#39;spam&#39;, &#39;ham&#39;])
3. Create a dataframe as shown below:
df=pd.DataFrame(data={&#39;a&#39;:np.random.randint(0,100,30),
&#39;b&#39;:np.random.randint(0, 100, 30), &#39;c&#39;:np.random.randint(0, 100, 30)})
a) Create a figure of size 15x8 with two subplots, top and bottom.
Draw two lines in the top axes, one green and one orange.
Add a legend for the top plot, Green and Orange. Put this legend in the top-
middle of graph.
Extra Challenge: In the bottom axes, create a graph of only the data points,
marked by circles, but with no line connecting the points.
b) Draw Bar graph for the above data.
4. According to the dataframe in Exercise 1:
a) Create a figure with three subplots, aligned vertically.
b) Create a bar graph for a and b on the first two,
c) Create a stacked bar graph by putting b on top of a
d) Design a pie chart for a and b
5. Language = [&#39;Java&#39;, &#39;Python&#39;, &#39;PHP&#39;, &#39;JavaScript&#39;, &#39;C#&#39;, &#39;C++&#39;]
Popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
Write a Python programming to display a
a) Bar chart of the popularity of programming Languages. Use different colour
for each bar.
b) Create a group bar chart by taking two consecutive elements from the
language list to form a group.
c) Create a stacked bar chart for the groups.
(Visualization styles: Provide suitable label in the x axis, y axis and a title,
legends, and border line)

Below are simple, exam-ready Python programs for all the questions. I’m using NumPy, Pandas, and Matplotlib.

First import:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
1. Minimum, Maximum, Average and Sum
def calculate(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    total = sum(numbers)

    return minimum, maximum, average, total


numbers = [10, 20, 30, 40, 50]

minimum, maximum, average, total = calculate(numbers)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)
print("Sum:", total)

Output:

Minimum: 10
Maximum: 50
Average: 30.0
Sum: 150
2. Count Each Class Label

Given:

labels = ['spam', 'ham', 'spam', 'spam', 'ham']
Using a dictionary:
def count_labels(labels):
    count = {}

    for label in labels:
        if label in count:
            count[label] += 1
        else:
            count[label] = 1

    return count


labels = ['spam', 'ham', 'spam', 'spam', 'ham']

result = count_labels(labels)

print(result)

Output:

{'spam': 3, 'ham': 2}
3. Create DataFrame
df = pd.DataFrame(data={
    'a': np.random.randint(0, 100, 30),
    'b': np.random.randint(0, 100, 30),
    'c': np.random.randint(0, 100, 30)
})

print(df)
3(a) Two Subplots
Figure size = 15 × 8
Top → two lines
Bottom → only points/circles
Legend at top-middle
fig, axes = plt.subplots(2, 1, figsize=(15, 8))

# Top graph
axes[0].plot(df['a'], color='green', label='Green')
axes[0].plot(df['b'], color='orange', label='Orange')

axes[0].set_title("Line Graph")
axes[0].set_xlabel("Index")
axes[0].set_ylabel("Values")

axes[0].legend(loc='upper center')

# Bottom graph - points only
axes[1].plot(df['c'], marker='o', linestyle='None')

axes[1].set_title("Data Points")
axes[1].set_xlabel("Index")
axes[1].set_ylabel("Values")

plt.tight_layout()
plt.show()
Important part for the extra challenge:
marker='o'
linestyle='None'

This gives circles without connecting lines.

3(b) Bar Graph
df.plot(kind='bar', figsize=(15, 8))

plt.title("Bar Graph")
plt.xlabel("Index")
plt.ylabel("Values")
plt.show()

Or using Matplotlib directly:

x = np.arange(len(df))

plt.figure(figsize=(15, 8))

plt.bar(x, df['a'], label='a')
plt.bar(x, df['b'], label='b')
plt.bar(x, df['c'], label='c')

plt.xlabel("Index")
plt.ylabel("Values")
plt.title("Bar Graph")
plt.legend()

plt.show()
4. DataFrame Visualization

Using the same df.

4(a), 4(b), 4(c), 4(d)

The question asks for three vertically aligned subplots.

fig, axes = plt.subplots(3, 1, figsize=(12, 15))

x = np.arange(len(df))

# -------------------------
# 1. Bar graph for a and b
# -------------------------

axes[0].bar(x - 0.2, df['a'], width=0.4, label='a')
axes[0].bar(x + 0.2, df['b'], width=0.4, label='b')

axes[0].set_title("Bar Graph of a and b")
axes[0].set_xlabel("Index")
axes[0].set_ylabel("Values")
axes[0].legend()


# -------------------------
# 2. Stacked bar graph
# -------------------------

axes[1].bar(x, df['a'], label='a')
axes[1].bar(x, df['b'], bottom=df['a'], label='b')

axes[1].set_title("Stacked Bar Graph")
axes[1].set_xlabel("Index")
axes[1].set_ylabel("Values")
axes[1].legend()


# -------------------------
# 3. Pie chart
# -------------------------

total_a = df['a'].sum()
total_b = df['b'].sum()

axes[2].pie(
    [total_a, total_b],
    labels=['a', 'b'],
    autopct='%1.1f%%'
)

axes[2].set_title("Pie Chart of a and b")


plt.tight_layout()
plt.show()
Remember the stacked bar concept:
plt.bar(x, a)
plt.bar(x, b, bottom=a)

bottom=a means b is placed on top of a.

5. Programming Language Popularity

Given:

Language = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']

Popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
5(a) Bar Chart with Different Colours
Language = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
Popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

colors = ['red', 'blue', 'green', 'orange', 'purple', 'yellow']

plt.figure(figsize=(10, 6))

plt.bar(Language, Popularity, color=colors, edgecolor='black')

plt.xlabel("Programming Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Languages")

plt.show()
5(b) Group Bar Chart

The question says:

Take two consecutive elements from the language list to form a group.

So the groups are:

Group 1 → Java, Python
Group 2 → PHP, JavaScript
Group 3 → C#, C++

Code:

Language = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
Popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

groups = ['Group 1', 'Group 2', 'Group 3']

x = np.arange(len(groups))
width = 0.35

plt.figure(figsize=(10, 6))

plt.bar(x - width/2,
        [Popularity[0], Popularity[2], Popularity[4]],
        width,
        label='First Language')

plt.bar(x + width/2,
        [Popularity[1], Popularity[3], Popularity[5]],
        width,
        label='Second Language')

plt.xlabel("Groups")
plt.ylabel("Popularity")
plt.title("Grouped Bar Chart")

plt.xticks(x, groups)
plt.legend()

plt.show()
5(c) Stacked Bar Chart
Language = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
Popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

groups = ['Group 1', 'Group 2', 'Group 3']

first = [Popularity[0], Popularity[2], Popularity[4]]
second = [Popularity[1], Popularity[3], Popularity[5]]

x = np.arange(len(groups))

plt.figure(figsize=(10, 6))

plt.bar(x, first, label='First Language')
plt.bar(x, second, bottom=first, label='Second Language')

plt.xlabel("Groups")
plt.ylabel("Popularity")
plt.title("Stacked Bar Chart")

plt.xticks(x, groups)
plt.legend()

plt.show()
🔥 Most important Matplotlib patterns to remember for your exam
Task	Code
Line graph	plt.plot(x, y)
Point-only graph	plt.plot(x, y, marker='o', linestyle='None')
Bar graph	plt.bar(x, y)
Horizontal bar	plt.barh(x, y)
Scatter plot	plt.scatter(x, y)
Pie chart	plt.pie(values)
Two subplots	plt.subplots(2, 1)
Figure size	figsize=(15, 8)
Legend	plt.legend()
Title	plt.title()
X-axis label	plt.xlabel()
Y-axis label	plt.ylabel()
Show graph	plt.show()
Stacked bar	plt.bar(x, b, bottom=a)
Different bar colors	plt.bar(x, y, color=colors)
Rotate x labels	plt.xticks(rotation=45)

For an exam, focus especially on: plot(), bar(), pie(), subplots(), legend(), xlabel(), ylabel(), title(), and bottom= for stacked bars.

before solving this give me some questions on numpy and pandas. proper ques and code, for lab assessnment. one ques, one solution

Absolutely. Let's do this like a lab assessment practice set rather than just random syntax questions.

I'll give you one proper question followed immediately by its solution, covering the NumPy and Pandas operations you're likely to be tested on.

NumPy + Pandas Lab Assessment Practice
Question 1 — NumPy Array Statistics

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
Solution
import numpy as np

marks = np.array([78, 85, 92, 67, 88, 76, 95, 81, 69, 90])

print("Array:", marks)
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))
print("Average:", np.mean(marks))
print("Total:", np.sum(marks))
print("Standard Deviation:", np.std(marks))
Question 2 — NumPy Array Creation

Question:
Create a NumPy array containing numbers from 10 to 50 with a step of 5. Then display:

The array
Number of elements
Shape
Data type
Solution
import numpy as np

arr = np.arange(10, 51, 5)

print("Array:", arr)
print("Number of elements:", arr.size)
print("Shape:", arr.shape)
print("Data type:", arr.dtype)

Expected array:

[10 15 20 25 30 35 40 45 50]
Question 3 — NumPy Reshaping

Question:
Create a NumPy array containing numbers from 1 to 12. Reshape it into a 3 × 4 matrix and display the matrix.

Then display:

First row
Last column
Element at second row and third column
Solution
import numpy as np

arr = np.arange(1, 13)

matrix = arr.reshape(3, 4)

print("Matrix:")
print(matrix)

print("First row:", matrix[0])
print("Last column:", matrix[:, -1])
print("Second row, third column:", matrix[1, 2])

Matrix:

[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
Question 4 — NumPy Random Numbers

Question:
Generate an array of 10 random integers between 1 and 100 using NumPy.

Find:

Maximum
Minimum
Mean
Sum
Solution
import numpy as np

arr = np.random.randint(1, 101, 10)

print("Array:", arr)
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))

Remember:

np.random.randint(1, 101, 10)

means 10 random integers from 1 to 100.

Question 5 — NumPy Filtering

Question:
Given:

marks = np.array([45, 78, 92, 34, 67, 88, 56, 91, 40, 73])

Write a program to:

Display all marks greater than 70.
Display all marks less than 50.
Count how many students scored more than 70.
Solution
import numpy as np

marks = np.array([45, 78, 92, 34, 67, 88, 56, 91, 40, 73])

print("Marks greater than 70:", marks[marks > 70])
print("Marks less than 50:", marks[marks < 50])
print("Number scoring above 70:", np.sum(marks > 70))

This is an important NumPy concept:

marks[marks > 70]
Question 6 — Create a Pandas Series

Question:
Create a Pandas Series containing the following temperatures:

32, 35, 31, 29, 36, 34, 30

Use the days of the week as the index.

Display:

The complete Series
Maximum temperature
Minimum temperature
Average temperature
Solution
import pandas as pd

temperature = pd.Series(
    [32, 35, 31, 29, 36, 34, 30],
    index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
)

print(temperature)

print("Maximum:", temperature.max())
print("Minimum:", temperature.min())
print("Average:", temperature.mean())
Question 7 — Create a DataFrame

Question:
Create the following DataFrame:

Name	Age	Marks
Ayan	20	85
Riya	21	92
Rahul	19	67
Sneha	20	78
Arjun	22	95

Write a program to display:

Complete DataFrame
First 3 rows
Last 2 rows
Information about the DataFrame
Statistical summary
Solution
import pandas as pd

data = {
    'Name': ['Ayan', 'Riya', 'Rahul', 'Sneha', 'Arjun'],
    'Age': [20, 21, 19, 20, 22],
    'Marks': [85, 92, 67, 78, 95]
}

df = pd.DataFrame(data)

print(df)

print("\nFirst 3 rows:")
print(df.head(3))

print("\nLast 2 rows:")
print(df.tail(2))

print("\nInformation:")
df.info()

print("\nStatistical Summary:")
print(df.describe())
Question 8 — Pandas Column Operations

Question:
Using the DataFrame from Question 7:

Display only the Name column.
Display only the Marks column.
Find the average marks.
Find the highest marks.
Find the lowest marks.
Solution
print(df['Name'])

print(df['Marks'])

print("Average Marks:", df['Marks'].mean())
print("Highest Marks:", df['Marks'].max())
print("Lowest Marks:", df['Marks'].min())
Question 9 — Pandas Filtering

Question:
Using the same DataFrame, display:

Students who scored more than 80.
Students whose age is 20.
Students who scored between 70 and 90.
Solution
print("Marks greater than 80:")
print(df[df['Marks'] > 80])

print("\nAge is 20:")
print(df[df['Age'] == 20])

print("\nMarks between 70 and 90:")
print(df[(df['Marks'] >= 70) & (df['Marks'] <= 90)])

This is very important for lab exams:

df[df['Marks'] > 80]
Question 10 — Add a New Column

Question:
Using the student DataFrame, create a new column called Result.

If marks are greater than or equal to 40, the result should be "Pass", otherwise "Fail".

Solution
df['Result'] = df['Marks'].apply(
    lambda x: 'Pass' if x >= 40 else 'Fail'
)

print(df)
Question 11 — Sorting

Question:
Using the student DataFrame:

Sort students according to marks in ascending order.
Sort students according to marks in descending order.
Sort students according to age.
'''

import pandas as pd

data = {
    'Name': ['Ayan', 'Riya', 'Rahul', 'Sneha', 'Arjun'],
    'Age': [20, 21, 19, 20, 22],
    'Marks': [85, 92, 67, 78, 95]
}

df = pd.DataFrame(data)
print(df)

print("first three rows: ", df.head(3))
print("")

print("information")
df.info()

print("statistical summary: ")
print(df.describe())

print(df['Name'])

print(df['Marks'])

print(df['Marks'].mean())
print(df['Marks'].max())

print(df[df['Marks']>80])

print(df[df['Age']==20])

print(sf[(df['Marks']>=70) & (df['Marks']<=90)])

print(df.sort_values('Marks', ascending=False))