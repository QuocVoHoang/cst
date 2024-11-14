import pandas as pd

file_path = 'origin.csv'
df = pd.read_csv(file_path)

df_length = df[['start_node', 'end_node', 'length']]
df_bikes = df[['start_node', 'end_node', 'bikes per hour']]
df_cars = df[['start_node', 'end_node', 'cars per hour']]

length_file_path = 'length.csv'
bikes_file_path = 'bikes_per_hour.csv'
cars_file_path = 'cars_per_hour.csv'

df_length.to_csv(length_file_path, index=False)
df_bikes.to_csv(bikes_file_path, index=False)
df_cars.to_csv(cars_file_path, index=False)

print(length_file_path, bikes_file_path, cars_file_path)
