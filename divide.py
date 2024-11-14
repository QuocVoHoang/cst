
import pandas as pd

# Đường dẫn đến file CSV gốc
file_path = 'undivided_matrix_length.csv'

# Đọc file CSV
data = pd.read_csv(file_path)

# Sao chép dữ liệu và chia các giá trị (trừ cột đầu tiên) cho 199
modified_data = data.copy()
modified_data.iloc[:, 1:] = round(modified_data.iloc[:, 1:] / 199, 0)

# Lưu dữ liệu đã chia vào file CSV mới
output_path = 'final_matrix_length.csv'
modified_data.to_csv(output_path, index=False)