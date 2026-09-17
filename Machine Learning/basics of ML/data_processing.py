import pandas as pd
import matplotlib.pyplot as plt

#Step 1: Import Libraries and Load Dataset

df = pd.read_csv(r"C:\Users\namra\OneDrive\Documents\Python-Journey\ML\basics of ML\diabetes.csv")
print(df.head())

#--Step2: inspect data ands check missing values

#print concise summary
print(df.info())

#returns the number of missing values per column
print(df.isnull().sum())

#--Step 3: Statistical Summary and Visualizing Outliers

#Computes count, mean, std deviation, min/max and quartiles for numerical columns.
print(df.describe())

#Visualize spread and detect outliers using matplotlib’s boxplot().
fig, axes = plt.subplots(len(df.columns), 1, figsize=(7,18), dpi=95)
'''
len(df.columns) → number of rows/subplots = number of columns in df
1 → 1 column of plots
figsize=(7, 18) → figure width = 7 inches, height = 18 inches
dpi=95 → resolution
'''
for i, col in enumerate(df.columns):
    axes[i].boxplot(df[col], vert=False)
    axes[i].set_ylabel(col)
plt.tight_layout()
plt.show()