import pandas as pd

# Load the dataset
data = pd.read_csv("dataset/Housing.csv")

# Display first 5 rows
print(data.head())

# Display dataset information
print(data.info())

# Display dataset size
print(data.shape)

# check the missing values
print(data.isnull().sum())

# Check duplicate records
print("Duplicate rows:", data.duplicated().sum())

# Check dataset columns
print(data.columns)

# Convert categorical data into numerical data
data = pd.get_dummies(data, drop_first=True)

# Display processed data
print(data.head())
print("New dataset shape:", data.shape)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Separate features and target
X = data.drop("price", axis=1)
y = data["price"]

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)
print("Model trained successfully!")

# Make predictions
y_pred = model.predict(X_test)

# Check model performance
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Absolute Error:", mae)
print("R2 Score:", r2)

import joblib
# Save trained model
joblib.dump(model, "model.pkl")
joblib.dump(X.columns.tolist(), "feature_columns.pkl")
print("Model saved successfully!")