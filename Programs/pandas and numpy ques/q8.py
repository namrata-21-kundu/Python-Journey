import pandas as pd

temp = pd.Series(
    [32, 35, 31, 29, 36, 34, 30],
    index = ['mon', 'tues', 'wed', 'thurs','fri', 'sat', 'sun']
)

print(temp)

print(temp.max())
print(temp.min())
print(temp.mean())