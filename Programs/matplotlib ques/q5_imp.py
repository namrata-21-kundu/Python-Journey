import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'C++', 'JavaScript']
popularity = [30, 35, 20, 15]

plt.pie(
    popularity,
    labels=languages,
    autopct='%1.1f%%'
)

plt.title("Programming Language Popularity")

plt.show()