def find_max(a, b, c):
    arr = sorted([a, b, c])
    return arr[2]


num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
k = 3
ans = []

# với 1 chu kỳ k = 3, thì sẽ luôn tồn tại 2 số cũ
full_cycles =  len(num_list) - (k - 1)

for i in range(full_cycles):
    ans.append(find_max(num_list[i], num_list[i + 1], num_list[i + 2]))

print(ans)