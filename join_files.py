import pandas as pd

def extract_city_data(city_name):
    # Read in each CSV file
    humidity = pd.read_csv('humidity.csv')
    pressure = pd.read_csv('pressure.csv')
    temp = pd.read_csv('temperature.csv')
    wind_dir = pd.read_csv('wind_direction.csv')
    wind_speed = pd.read_csv('wind_speed.csv')
    weather_desc = pd.read_csv('weather_description.csv')

    # Extract data for the specified city
    humid_city = humidity[['datetime', city_name]]
    press_city = pressure[['datetime', city_name]]
    temp_city = temp[['datetime', city_name]]
    wind_dir_city = wind_dir[['datetime', city_name]]
    wind_speed_city = wind_speed[['datetime', city_name]]
    weather_desc_city = weather_desc[['datetime', city_name]]

    # Rename value columns
    humid_city = humid_city.rename(columns={city_name: 'humidity'})
    press_city = press_city.rename(columns={city_name: 'pressure'})
    temp_city = temp_city.rename(columns={city_name: 'temperature'})
    wind_dir_city = wind_dir_city.rename(columns={city_name: 'wind_direction'})
    wind_speed_city = wind_speed_city.rename(columns={city_name: 'wind_speed'})
    weather_desc_city = weather_desc_city.rename(columns={city_name: 'weather_desc'})

    # Merge into a single DataFrame
    merged_city = humid_city.merge(press_city, on='datetime')
    merged_city = merged_city.merge(temp_city, on='datetime')
    merged_city = merged_city.merge(wind_dir_city, on='datetime')
    merged_city = merged_city.merge(wind_speed_city, on='datetime')
    merged_city = merged_city.merge(weather_desc_city, on='datetime')

    # Set index as datetime
    merged_city = merged_city.set_index('datetime')

    # Replace spaces with underscores in the output file name
    output_file = f'{city_name.replace(" ", "_").lower()}_weather.csv'

    # Write to CSV file
    merged_city.to_csv(output_file)

# Example: Let the user input the desired city
user_city = input("Enter the city name: ")
extract_city_data(user_city)
