import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

df = pd.read_csv('san_francisco_weather_cleaned.csv')

# Features and target variable
features = ['humidity', 'pressure', 'temperature', 'wind_direction', 'wind_speed']
target = 'weather_desc'

# Separate features and target
X = df[features]
y = df[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply SMOTE to the training data only
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Create a new DataFrame with the resampled data
df_resampled = pd.DataFrame(X_train_resampled, columns=features)
df_resampled[target] = y_train_resampled

# Write the resampled data to a new CSV file
df_resampled.to_csv('san_francisco_weather_cleaned_resampled.csv', index=False)
