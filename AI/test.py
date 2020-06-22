import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


''' Read Data.csv '''
dataset = pd.read_csv('DevNet/AI/Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
# print(x)
# print(y)


''' Take care of missing values '''
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
# print(X)


''' Turn strings into numerical values [Countries]'''
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])] , remainder='passthrough')
X = np.array(ct.fit_transform(X))
# print(X)


''' Turn strings into numerical values [Booleans]'''
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
# print(y)


''' Splitting the dataset into the Training set and Test set '''
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=1)
# print(X_train)
# print(X_test)
# print(y_train)
# print(y_test)
''' Feature Scaling '''
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.transform(X_test[:, 3:])
print(X_train)
print(X_test)