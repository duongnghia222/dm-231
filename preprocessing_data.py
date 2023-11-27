import pandas as pd

# Read in DataFrame
# df = pd.read_csv('san_francisco_weather.csv')
df = pd.read_csv('los_angeles_weather.csv')

# Numeric columns
num_cols = ['humidity', 'pressure', 'temperature', 'wind_speed']

# Text columns
text_cols = ['weather_desc']

print("Rows before cleaning: ", len(df))

# Drop rows with text NaNs
df.dropna(subset=text_cols, inplace=True)


# Interpolate 'humidity' column separately
df['humidity'].interpolate(method='nearest', limit_direction='both', inplace=True)

# Interpolate other numeric NaNs with the mean of 10 nearest numeric values
for col in num_cols[1:]:
    df[col].interpolate(method='nearest', limit_direction='both', inplace=True)

# Drop remaining rows with NaN values
df.dropna(inplace=True)

# Convert temperature from Kelvin to Celsius
df['temperature'] = df['temperature'] - 273.15

# Calculate the IQR (Interquartile Range)
Q1 = df[num_cols].quantile(0.25)
Q3 = df[num_cols].quantile(0.75)
IQR = Q3 - Q1

# Define the threshold for identifying outliers
threshold = 1.5

# Identify and remove outliers
outliers = ((df[num_cols] < (Q1 - threshold * IQR)) | (df[num_cols] > (Q3 + threshold * IQR))).any(axis=1)
df_no_outliers = df.loc[~outliers]

# Display information about the removal
print("Number of rows before removing outliers:", len(df))
print("Number of rows after removing outliers:", len(df_no_outliers))
df = df_no_outliers.copy()


print("Rows after cleaning: ", len(df))

# Check for remaining NaN values before writing to CSV
nan_check = df.isnull().sum()
print("NaN check before writing to file:")
print(nan_check)

unique_values_counts = df['weather_desc'].value_counts()
print(unique_values_counts)
# Filter labels with count >= 100
labels_to_keep = unique_values_counts[unique_values_counts >= 10].index

# Create a new DataFrame with only the selected labels
df = df[df['weather_desc'].isin(labels_to_keep)]

# Display the unique values and their counts after filtering
print(df['weather_desc'].value_counts())

print(df['weather_desc'].unique())
# Apply weather conditions logic to 'weather_desc' column
weather_conditions_dict = {}

special_cases = {
    'mist': 'foggy',
    'frog': 'foggy',
    'haze': 'clear',
    'smoke': 'clear',
    'thunderstorm with light rain': 'severe',
    'light intensity drizzle': 'rain',
    'thunderstorm with rain': 'severe',
    'thunderstorm with heavy rain': 'severe',
    'light thunderstorm': 'severe',
    'thunderstorm': 'severe',
}

for weather_condition in df['weather_desc'].unique():
    weather_condition_lowered = weather_condition.lower()

    for key, value in special_cases.items():
        if key.lower() in weather_condition_lowered:
            weather_conditions_dict[weather_condition] = value
            break
    else:
        if 'thunderstorm' in weather_condition_lowered:
            weather_conditions_dict[weather_condition] = 'severe'

        elif 'rain' in weather_condition_lowered:
            weather_conditions_dict[weather_condition] = 'rain'

        elif 'snow' in weather_condition_lowered:
            weather_conditions_dict[weather_condition] = 'snow'

        elif 'cloud' in weather_condition_lowered:
            weather_conditions_dict[weather_condition] = 'cloudy'

        elif any(key in weather_condition_lowered for key in ['clear', 'sun']):
            weather_conditions_dict[weather_condition] = 'clear'

print(weather_conditions_dict)

# Map the weather conditions to the DataFrame
df['weather_desc'] = df['weather_desc'].map(weather_conditions_dict)

# Drop rows with text NaNs
df.dropna(subset=text_cols, inplace=True)

unique_values_after = df['weather_desc'].nunique()
print(f"Number of unique values in 'weather_desc' after processing: {unique_values_after}")

# Display the unique values and their counts after filtering
print(df['weather_desc'].value_counts())

# Check for remaining NaN values again after processing
nan_check_after = df.isnull().sum()
print("NaN check after processing:")
print(nan_check_after)





# Write cleaned data to CSV
# df.to_csv('san_francisco_weather_cleaned.csv', index=False)
df.to_csv('los_angeles_weather_cleaned.csv', index=False)
