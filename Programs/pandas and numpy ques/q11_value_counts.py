import pandas as pd

labels = ['spam', 'ham', 'spam', 'spam', 'ham', 'promotion', 'ham']

series = pd.Series(labels)

print(series.value_counts())