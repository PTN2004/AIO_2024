import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Read dataset using pandas (pd)
dataset_path = "./data/Housing.csv"
df = pd.read_csv(dataset_path)

# process categorical data
categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()

ordinal_encoder = OrdinalEncoder()
encoder_categorical_cols = ordinal_encoder.fit_transform(df[categorical_cols])
encoder_categorical_df = pd.DataFrame(encoder_categorical_cols, columns=categorical_cols)

numerical_df = df.drop(categorical_cols, axis=1)
encoded_df = pd.concat([numerical_df, encoder_categorical_df], axis=1)

standard_scaler = StandardScaler()
dataset_arr = standard_scaler.fit_transform(encoded_df)

# Splitter data
X, y = dataset_arr[:, 1:], dataset_arr[:, 0]

test_size = 0.3
random_state = 1

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=random_state, test_size=test_size, shuffle=True)

# Train model
rf_regressor = RandomForestRegressor(random_state=random_state)
ab_regressor = AdaBoostRegressor(random_state=random_state)
gb_regressor = GradientBoostingRegressor(random_state=random_state)

# fit data
rf_regressor.fit(X_train, y_train)
ab_regressor.fit(X_train, y_train)
gb_regressor.fit(X_train, y_train)

# Predict and evaluate
rf_y_pre = rf_regressor.predict(X_test)
ab_y_pre = ab_regressor.predict(X_test)
gb_y_pre = gb_regressor.predict(X_test)

rf_score_MSE = mean_squared_error(y_test, rf_y_pre)
ab_score_MSE = mean_squared_error(y_test, ab_y_pre)
gb_score_MSE = mean_squared_error(y_test, gb_y_pre)

rf_score_MAE = mean_absolute_error(y_test, rf_y_pre)
ab_score_MAE = mean_absolute_error(y_test, ab_y_pre)
gb_score_MAE = mean_absolute_error(y_test, gb_y_pre)
