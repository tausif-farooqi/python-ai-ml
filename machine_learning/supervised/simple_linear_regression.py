import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Program to demonstrate simple linear regression. The data used is a salary dataset with years of experience and salary.

# Load the salaray  dataset
# The dataset can be downloaded from 
# https://www.kaggle.com/datasets/abhishek14398/salary-dataset-simple-linear-regression/data
data = pd.read_csv('./data_sets/salary_dataset.csv')
print(data.head())

data.drop(columns=['Unnamed: 0'], inplace=True)

# Define features and target variable
X = data[['YearsExperience']]
y = data['Salary']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
from sklearn import linear_model

model = linear_model.LinearRegression()
model.fit(X_train, y_train)

coef = model.coef_[0]
intercept = model.intercept_

print(f"Model Coefficient: {coef}")
print(f"Model Intercept: {intercept}") 

# Visualize the fit of the model to the training data
plt.scatter(X_train, y_train,  color='blue')
plt.plot(X_train, coef * X_train + intercept, '-r')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

# Make predictions
y_pred = model.predict(X_test)

# evaluate the predictions
print("Mean absolute error: %.2f" % mean_absolute_error(y_test, y_pred))
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
print("Root mean squared error: %.2f" % np.sqrt(mean_squared_error(y_test, y_pred)))
print("R2-score: %.2f" % r2_score(y_test, y_pred))