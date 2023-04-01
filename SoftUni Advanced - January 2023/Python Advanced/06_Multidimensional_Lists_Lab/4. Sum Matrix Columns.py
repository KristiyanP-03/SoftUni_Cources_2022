rows, cols = input().split(", ")
rows = int(rows)
cols = int(cols)
matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(' ')])

for i in range(cols):
    col_sum = 0
    for j in range(rows):
        col_sum += matrix[j][i]
    print(col_sum)