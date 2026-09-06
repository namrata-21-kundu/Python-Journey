import matplotlib.pyplot as plt

subjects = ['Math', 'Science', 'English']

boys = [80, 75, 85]
girls = [85, 90, 88]

plt.bar(subjects, boys, label='Boys')
plt.bar(subjects, girls, bottom=boys, label='Girls')

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Stacked Bar Chart")

plt.legend()

plt.show()