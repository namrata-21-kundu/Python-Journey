'''
Question:
Create a DataFrame containing 20 rows and three columns A, B, and C. Each column should contain 20 random integers between 0 and 100.

Then:

Display the DataFrame.
Find the average of each column.
Find the maximum value of each column.
Find the minimum value of each column.
Add a new column Total containing the sum of A, B and C.
Display the 5 rows with the highest total.
'''

import numpy as np
import pandas as pd

df = pd.DataFrame({
        'A': np.random.randint(0,101,20),
        'B': np.random.randint(0,101,20),
        'C': np.random.randint(0,101,20)
    })

print("Datafarme:" )
print(df)

print("Average: ")
print(df[['A', 'B', 'C']].mean())

print("Maximum: ")
print(df[['A', 'B', 'C']].max())

df['Total']=df['A']+df['B']+df["C"]