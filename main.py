
import numpy as np

import pandas as pd

from sklearn.model_selection import train_test_split, cross_val_score

from sklearn.metrics import mean_squared_error

 


# Models to try with

from sklearn.linear_model import LinearRegression, Lasso, Ridge

from sklearn.svm import SVR

from sklearn.tree import DecisionTreeRegressor

from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

from sklearn.neighbors import KNeighborsRegressor




# 0. Read dataset

data = pd.read_csv("./dataset_00_with_header.csv")

print(data.head(n=1))



# 1. Handle empty Values

print("Handling empty values...")

# data = data.interpolate(method='linear')

data = data.fillna(data.median())

# print(data.head(n=1))



# 2. Prepare dataset

print("Preparing dataset...")

X = data.drop('y', axis=1)

y = data['y']

 


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# 3. Create a list of models to try:

print("Preparing model candidates...")

models = [

 ('Linear Regression', LinearRegression()),

 ('Lasso', Lasso()),

 ('Ridge', Ridge()),

 ('Support Vector Regression', SVR()),

 ('Decision Tree', DecisionTreeRegressor()),

 ('Random Forest', RandomForestRegressor()),

 ('Gradient Boosting', GradientBoostingRegressor()),

 ('K-Nearest Neighbors', KNeighborsRegressor())

]



# 4. Train and cross-validate each model:

print("Training & validating...")

results = []

 


for name, model in models:

 cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='neg_mean_squared_error')

 rmse_scores = np.sqrt(-cv_scores)

 mean_rmse = np.mean(rmse_scores)

 results.append((name, mean_rmse))

 print(f"{name}: RMSE = {mean_rmse}")

 


# 5. Compare the performance of each model:

print("Comparing models...")

results_df = pd.DataFrame(results, columns=['Model', 'RMSE'])

results_df = results_df.sort_values('RMSE', ascending=True)

 


print("Models ranked by RMSE:")

print(results_df)



# 6. Save to file

np.save("result.txt", results_df)
