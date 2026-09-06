'''
Question:
Create a figure of size 12 × 10 with three vertically aligned subplots:

Bar graph
Line graph
Pie chart
'''

import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'C++', 'JavaScript']
popularity = [30, 35, 20, 15]

fig, axes = plt.subplots(3, 1, figsize=(12, 10))

# 1. Bar graph
axes[0].bar(languages, popularity, edgecolor='black')
axes[0].set_title("Bar Chart")
axes[0].set_xlabel("Languages")
axes[0].set_ylabel("Popularity")

# 2. Line graph
axes[1].plot(languages, popularity, marker='o')
axes[1].set_title("Line Chart")
axes[1].set_xlabel("Languages")
axes[1].set_ylabel("Popularity")

# 3. Pie chart
axes[2].pie(
    popularity,
    labels=languages,
    autopct='%1.1f%%'
)
axes[2].set_title("Pie Chart")

plt.tight_layout()
plt.show()