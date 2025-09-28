import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing

# Program to demonstrate multiple linear regression. The data used is a student scores dataset with multiple features.
# Load the student  dataset
# The dataset can be downloaded from 
# https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression
data = pd.read_csv('./data_sets/student_performance.csv')

# Convert categorical (Yes/No) data to numerical
label_encoder = LabelEncoder()
data['Extracurricular Activities'] = label_encoder.fit_transform(data['Extracurricular Activities']) 

# Display the first few rows and some information of the dataset
print("First few rows of the dataset:")
print(data.head())
print("\nDataset Information:")
print(data.info())

correlation_values = data.corr()['Performance Index'].drop('Performance Index')
print("\nCorrelation with Performance Index:")
print(correlation_values)

# check how many are missing
print("\nMissing values in each column:")
print(data.isnull().sum())

# Define features and target variable
X = data.iloc[:, :-1]  # Features: all columns except the last
y = data.iloc[:, -1]   # Target: last column (Performance Index)

# Standardize the feature variables
X = preprocessing.StandardScaler().fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train the model
from sklearn import linear_model
model = linear_model.LinearRegression()
model.fit(X_train, y_train)

coef = model.coef_
intercept = model.intercept_
print(f"\nModel Coefficients: {coef}")
print(f"Model Intercept: {intercept}")

# Make predictions
y_pred = model.predict(X_test)
# evaluate the predictions
print("\nMean absolute error: %.4f" % mean_absolute_error(y_test, y_pred))
print("Mean squared error: %.4f" % mean_squared_error(y_test, y_pred))
print("Root mean squared error: %.4f" % np.sqrt(mean_squared_error(y_test, y_pred)))
print("R2-score: %.4f" % r2_score(y_test, y_pred))

# Visualize the fit of the model to the test data
plt.scatter(y_test, y_pred, color='blue')
plt.xlabel("Actual Performance Index")
plt.ylabel("Predicted Performance Index")
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
plt.show()
