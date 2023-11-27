import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Read in DataFrame
df = pd.read_csv('san_francisco_weather_cleaned.csv')

# Convert 'datetime' to datetime format
df['datetime'] = pd.to_datetime(df['datetime'])

# Filter data for the year 2016
df_2016 = df[df['datetime'].dt.year == 2016]

# Extract numeric columns for visualization
numeric_columns = ['humidity', 'pressure', 'temperature', 'wind_direction', 'wind_speed']

# Separate features and target variable
X = df_2016[numeric_columns]

# Standardize the features
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)

# Perform PCA to reduce dimensionality to 2 components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_standardized)

# Visualize PCA results for 2016
plt.figure(figsize=(6, 5))
plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.title('PCA Visualization for 2016')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()
