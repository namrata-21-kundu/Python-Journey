'''
Question:
Create this DataFrame:

data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Marks': [80, None, 90, None]
}

Write a program to:

Check for missing values.
Count missing values.
Replace missing marks with the average marks.
'''

import pandas as pd

data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Marks': [80, None, 90, None]
}

df = pd.DataFrame(data)

#missing value
print("missing value")
print(df.isnull())

print("count missing value: ")
print(df.isnull().sum())

average_marks = df['Marks'].mean()
#replace with mean
df['Marks'] = df['Marks'].fillna(average_marks)
print(df)