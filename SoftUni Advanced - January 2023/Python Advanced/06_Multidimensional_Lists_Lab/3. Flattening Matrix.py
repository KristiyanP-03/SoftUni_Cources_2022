rows = int(input())
matrix = []

for row in range(rows):
    # matrix.append(list(map(int, input().split(", "))))
    matrix.append([int(x) for x in input().split(", ")])

# flattened_matrix = [num for row in matrix for num in row]
flattened_matrix = []
for row in matrix:
    for num in row:
        flattened_matrix.append(num)

print(flattened_matrix)