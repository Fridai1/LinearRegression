#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import explained_variance_score 
from sklearn.metrics import max_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error


# importing Dataset

# dataset = pd.read_excel(open('parking-estimation.xlsx', 'rb'))
dataset = pd.read_csv('csvParking.csv', decimal=',')

X = dataset.iloc[:,2:6].values
y = dataset.iloc[:,1:2].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)



# accuracy in %
explained_variance_score(y_test, y_pred)
max_error(y_test, y_pred)
r2_score(y_test, y_pred)


