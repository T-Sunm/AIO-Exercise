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


# ----------C2-----------
# vì 3 phần tử cuối kh cần duyệt nên - k , dễ nhìn thấy - k đi thì vẫn còn dư 1 phần tử ở cuối nên + 1
start_indexs = list(range(0, len(num_list) - k + 1))
# vì slicing phần end là [start:end - 1] nên end_index cần cộng lên 1
end_indexs = list(range(k, len(num_list) + 1))

for start_index, end_index in zip(start_indexs, end_indexs):
  sub_list = num_list[start_index: end_index]
  print(max(sub_list))

# ----------C3-----------
sub_list = list()
for data in num_list:
  sub_list.append(data)
  if len(sub_list) == k:
    print(max(sub_list))
    sub_list.pop(0)
