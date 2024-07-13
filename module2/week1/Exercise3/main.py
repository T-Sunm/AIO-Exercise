import numpy as np
import pandas as pd
import os
import gdown

# URL tệp trên Google Drive
url = 'https://drive.google.com/uc?id=1iA0WmVfW88HyJvTBSQDI5vesf-pgKabq'

# Lấy đường dẫn tuyệt đối của tập lệnh hiện tại
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

# Thư mục đích
output_folder = os.path.join(script_dir, 'data')

# Tên tệp đích
output_file = 'advertising.csv'

# Tạo thư mục nếu chưa tồn tại
if not os.path.exists(output_folder):
  os.makedirs(output_folder)

# Đường dẫn đầy đủ tới tệp đích
output_path = os.path.join(output_folder, output_file)

# Tải tệp
gdown.download(url, output_path, quiet=False)

print(f"Tệp đã được tải về: {output_path}")

df = pd.read_csv('module2/week1/Exercise3/data/advertising.csv')

data = df.to_numpy()
print(df)

# câu 15:
# cách 1:
max_sales = df['Sales'].max()
maxid_sales = df['Sales'].idxmax()

# cách 2:
max_sales = np.max(data[:, 3])
maxid_sales = np.argmax(data[:, 3])
print(f"Câu 15 : Max: {max_sales} - Index: {maxid_sales}")

# câu 16:
# cách 1:
mean_val = np.round(df['TV'].mean(), 1)

# cách 2:
mean_val = np.round(data[:, 0].mean(), 1)
print(f"Câu 16 : {mean_val}")

# câu 17:
# cách 1:
sales_gt = df.loc[df['Sales'] >= 20]
c_sales = sales_gt['Sales'].count()

# cách 2
sales = data[:, 3]
c_sales = np.count_nonzero(sales[sales >= 20])
print(f"Câu 17 : {c_sales}")

# câu 18:
# cách 1:
filter_data = df.loc[df['Sales'] >= 15]
average_radio = np.round(filter_data['Radio'].mean(), 1)

# cách 2
condition = data[:, 3] >= 15
filter_data = data[condition]
average_radio = np.round(filter_data[:, 1].mean(), 1)
print(f"Câu 18 : {average_radio}")

# câu 19:
# cách 1
mean_newspaper = df['Newspaper'].mean()
filter_data = df.loc[df['Newspaper'] > mean_newspaper]
sum_sales = round(filter_data['Sales'].sum(), 1)

# cách 2
mean_newspaper = data[:, 2].mean()
condition = data[:, 2] >= mean_newspaper
filter_data = data[condition]
sum_sales = round(filter_data[:, 3].sum(), 1)
print(f"Câu 19 : {sum_sales}")

# câu 20
rating = ['Good', 'Average', 'Bad']
# cách 1:
sales = df['Sales']
mean_sales = sales.mean()
scores = np.where(sales > mean_sales, rating[0], np.where(
    sales == mean_sales, rating[1], rating[2]))

# cách 2:
mean_sales = np.round(data[:, 3].mean(), 1)
condition_good = data[:, 3] > mean_sales
condition_average = data[:, 3] == mean_sales
scores = np.where(condition_good, rating[0], np.where(
    condition_average, rating[1], rating[2]))
print(f"Câu 20 : {scores[7:10]}")

# câu 21 : Gọi giá trị trên cột Sales gần nhất với giá trị trung bình(khoảng cách giá trị với mean_sales nhỏ nhất)
# cũng chính cột Sales là A.
rating = ['Good', 'Average', 'Bad']
# cách 1:
sales = df['Sales']
mean_sales = sales.mean()
idx_min = np.abs(sales - mean_sales).argmin()
A = sales.iloc[idx_min]
scores = np.where(sales > A, rating[0], np.where(
    sales == A, rating[1], rating[2]))

# cách 2:
sales = data[:, 3]
mean_sales = sales.mean()
normalize_sales = np.abs(sales - mean_sales)
A = sales[normalize_sales.argmin()]
scores = np.where(sales > A, rating[0], np.where(
    sales == A, rating[1], rating[2]))
print(f"Câu 21 : {scores[7:10]}")
