import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("heart.csv")

df.shape #shape

df.isnull().sum() #missing values

df.dtypes

(df==0).sum() #count zeroes

df["Age"].mean()

new_df = df[["Age", "Sex", "ChestPain", "RestBP", "CHol"]]

train,test = train_test_split(
    new_df,
    test_size=0.25,
    random_state=42
)

print("training data shape: ", train.shape)
print("testing data shape: ", test.shape)

#[part 2]
from sklearn.metrices import confusion_matrrix, accuracy_score
from sklearn.metrices import precision_score, recall_score, f1_score

# Actual and predicted values
actual = [1] * 50 + [0] * 450

predicted = [1] * 45 + [0] * 5 + [1] * 55 + [0] * 395

cm = confusion_matrrix(actual, predicted)
print(cm)

print(accuracy_score(actual, predicted))
print(precision_score(actual, predicted))
print(recall_score(actual, predicted))
print(f1_score(actual,predicted))

'''
* **TP (True Positive)** = Actually Positive AND Predicted Positive
* **FP (False Positive)** = Actually Negative BUT Predicted Positive
* **FN (False Negative)** = Actually Positive BUT Predicted Negative
* **TN (True Negative)** = Actually Negative AND Predicted Negative

'''