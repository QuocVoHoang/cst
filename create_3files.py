import pandas as pd

# Đường dẫn tới file gốc
file_path = 'origin.csv'

# Đọc file CSV gốc
df = pd.read_csv(file_path)

# Tách dữ liệu thành 3 DataFrame khác nhau
df_length = df[['start_node', 'end_node', 'length']]
df_bikes = df[['start_node', 'end_node', 'bikes per hour']]
df_cars = df[['start_node', 'end_node', 'cars per hour']]

# Đường dẫn tới các file đầu ra
length_file_path = 'length.csv'
bikes_file_path = 'bikes_per_hour.csv'
cars_file_path = 'cars_per_hour.csv'

# Lưu từng DataFrame thành file CSV riêng
df_length.to_csv(length_file_path, index=False)
df_bikes.to_csv(bikes_file_path, index=False)
df_cars.to_csv(cars_file_path, index=False)

# In ra đường dẫn các file đã tạo
print(length_file_path, bikes_file_path, cars_file_path)
