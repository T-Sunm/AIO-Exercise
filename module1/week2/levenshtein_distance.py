def levenshtein_distance(s, t):
  rows = len(s) + 1
  cols = len(t) + 1

  # Khởi tạo ma trận zero với kích thước (rows x cols)
  matrix = [[0] * cols for _ in range(rows)]

  # Điền giá trị cho cột 0 và hàng 0
  for i in range(rows):
    matrix[i][0] = i
  for j in range(cols):
    matrix[0][j] = j

  # Tính toán khoảng cách chỉnh sửa
  for i in range(1, rows):
    for j in range(1, cols):
      if S[i - 1] == T[j - 1]:
        matrix[i][j] = matrix[i - 1][j - 1]
      else:
        del_cost = matrix[i - 1][j]    # Chi phí xóa
        ins_cost = matrix[i][j - 1]    # Chi phí chèn
        sub_cost = matrix[i - 1][j - 1]  # Chi phí thay thế
        matrix[i][j] = min(del_cost, ins_cost, sub_cost) + 1

  # Giá trị ở góc dưới bên phải của ma trận là khoảng cách Levenshtein
  return matrix[rows - 1][cols - 1]


# Ví dụ sử dụng
S = 'adceg'
T = 'abcfg'
print("Khoảng cách Levenshtein:", levenshtein_distance(S, T))
