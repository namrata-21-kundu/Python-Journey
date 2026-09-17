import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv(r"C:\Users\namra\OneDrive\Documents\Python-Journey\ML\basics of ML\headbrain1.csv")
print(df.head())

x = df['Head Size(cm^3)']
y= df['Brain Weight(grams)']

x_train, x_test, y_train, y_test= train_test_split(x, y, random_state=104, test_size=0.25, shuffle=True)

 # printing out train and test sets

print('X_train : ')
print(x_train.head())
print('')
print('X_test : ')
print(x_test.head())
print('')
print('y_train : ')
print(y_train.head())
print('')
print('y_test : ')
print(y_test.head())