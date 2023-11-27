import pandas as pd
import matplotlib.pyplot as plt

# Load data into Pandas DataFrame
df = pd.read_csv('san_francisco_weather_cleaned.csv')

# Convert datetime to Pandas datetime
df['datetime'] = pd.to_datetime(df['datetime'])

# Filter data for the year 2016
df_2016 = df[(df['datetime'] >= '2016-01-01') & (df['datetime'] <= '2016-12-31')]

# Plot humidity over time in 2016
plt.figure()
df_2016.plot(x='datetime', y='humidity')
plt.xticks(rotation=45)
plt.title('Humidity Over Time in 2016')

# Plot pressure over time in 2016
plt.figure()
df_2016.plot(x='datetime', y='pressure')
plt.xticks(rotation=45)
plt.title('Pressure Over Time in 2016')

# Plot temperature over time in 2016
plt.figure()
df_2016.plot(x='datetime', y='temperature')
plt.xticks(rotation=45)
plt.title('Temperature Over Time in 2016')

# Scatter plot of temperature vs humidity
plt.figure(figsize=(8, 6))
plt.scatter(df_2016['temperature'], df_2016['humidity'], alpha=0.5)
plt.title('Relationship between Temperature and Humidity (2016)')
plt.xlabel('Temperature (Celsius)')
plt.ylabel('Humidity (%)')
plt.grid(True)


plt.tight_layout()
plt.show()
