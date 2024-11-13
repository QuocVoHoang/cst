import pandas as pd

# Đường dẫn tới các tệp
matrix_bike_path = 'matrix_length.csv'
locations_path = 'locations200.csv'

# Đọc các tệp CSV
matrix_bike = pd.read_csv(matrix_bike_path, index_col=0)
locations = pd.read_csv(locations_path)

# Chuyển đổi node_id trong DataFrame locations thành chuỗi để khớp
locations['node_id'] = locations['node_id'].astype(str)

# Tạo từ điển để ánh xạ node_id với location
node_to_location = dict(zip(locations['node_id'], locations['location']))

# Cập nhật chỉ mục hàng và cột đầu bằng location nếu node_id trùng khớp
matrix_bike.index = [node_to_location.get(str(node), node) for node in matrix_bike.index]
matrix_bike.columns = [node_to_location.get(str(node), node) for node in matrix_bike.columns]

# Lưu DataFrame đã cập nhật vào tệp final_matrix_bike.csv
final_matrix_bike_path = 'final_matrix_length.csv'
matrix_bike.to_csv(final_matrix_bike_path)