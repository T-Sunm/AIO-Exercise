def compute_levenshtein(S, T):

    return


S = 'adceg'
T = 'abcfg'
matrix = []

first_column_value = 1
matrix.append([j for j in range(len(T) + 1)])
for i in range(1, len(S) + 1):
    row = []
    for j in range(len(T) + 1):
        if j == 0:
            row.append(first_column_value)
            first_column_value += 1
        else:
            row.append(0)
    matrix.append(row)

print(matrix)

for i in range(1, len(S) + 1):
    for j in range(1, len(T) + 1):
        if (T[j - 1] == S[i - 1]):
            matrix[i][j] = matrix[i - 1][j - 1]
        else:
            del_cost = matrix[i - 1][j]
            ins_cost = matrix[i][j - 1]
            sub_cost = matrix[i - 1][j - 1]
            matrix[i][j] = min(del_cost, ins_cost, sub_cost) + 1

print(matrix)
