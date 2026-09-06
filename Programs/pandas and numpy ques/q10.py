'''
Question:
Create the following DataFrame:

Name    Department    Salary
A       IT            40000
B       HR            35000
C       IT            50000
D       HR            45000
E       Sales         30000
F       Sales         40000

Use groupby() to find the average salary of each department.
'''

import pandas as pd

data = {
    'Name': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Department': ['IT', 'HR', 'IT', 'HR', 'Sales', 'Sales'],
    'Salary': [40000, 35000, 50000, 45000, 30000, 40000]
}

df = pd.DataFrame(data)

result = df.groupby('Department')['Salary'].mean()

