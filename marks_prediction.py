# -*- coding: utf-8 -*-
"""Marks Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IJ4jnQcdiwFSvaABbfh-KyWy8ULyaSB0

**Importing Libaries**
"""

from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

"""**Load Dataset**"""

Scores = pd.read_csv("https://bit.ly/w-data")

"""**Load Summarize**"""

print(Scores.shape)
print(Scores.head(5))
print(Scores.describe())

"""**Finding and Removing NULL values from our feature X**"""

Scores.columns[Scores.isna().any()]
#here we are checking is any null value exist in this dataset or not

#if any NULL value present in the dataset so we can remove that
#Scores.Hours = Scores.Hours.fillna(Scores.Hours.mean())
#datasetname.column(NULLvalue) = datasetname.column(nullvalue).fillna(datasetname.coulum(nullvalue).mean())

"""**Segregate Dataset into input X & output Y**"""

X = Scores.iloc[:, :-1].values
print(X.shape)
X
#converting complete dataset into a array

Y = Scores.iloc[:, -1].values
Y

from sklearn.model_selection import train_test_split 
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 0)

"""**Training Dataset using Linear Regressio**

**Visulaisation and Analysis**
"""

#training our data using linear regression
model = LinearRegression()
model.fit(X_train,Y_train)

#plotting the regression line
line = model.coef_*X+model.intercept_

#plotting for the test data
plt.scatter(X,Y,color = "blue")
plt.plot(X, line, color='green')
plt.xlabel("Hours")
plt.ylabel("Percentage")
plt.show()

"""**Making Prediction**"""

model.coef_

model.intercept_

model.score(X,Y)

PredictedmodelResult = model.predict(X_test)  #testing data in hours
print(f"Predicted Score is = {PredictedmodelResult}") #scores prediction

#we can take any random data 
a = [[6.2]]  # a is our random data which is denoting to number of hours
Prediction = model.predict(a)
print(Prediction)

"""**Comparing Actual REsult vs Predicted Result**"""

Scores = pd.DataFrame({"Actual Data": Y_test, "Predicted Data": PredictedmodelResult})
Scores

plt.figure()
plt.plot(Y_test, color = "blue", label = "Actual Data")
plt.plot(PredictedmodelResult, color = "green", label = 'Predicted Data')
plt.title("Actual VS Predicted")
plt.xlabel("Study Hrs ")
plt.ylabel("Percentage")
plt.legend()

