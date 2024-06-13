num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
max_values = []

# Số chu kỳ đầy đủ để trượt cửa sổ kích thước k
full_cycles = len(num_list) - (k - 1)

# Tính max cho mỗi cửa sổ trượt
for i in range(full_cycles):
  # Tính max từ index hiện tại i đến i+k
  current_max = max(num_list[i:i + k])
  max_values.append(current_max)

print(max_values)
