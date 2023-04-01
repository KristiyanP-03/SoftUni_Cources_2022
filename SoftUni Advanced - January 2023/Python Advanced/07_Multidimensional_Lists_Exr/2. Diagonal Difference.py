rows = int(input())
matrix = []

for i in range(rows):
    matrix.append([int(x) for x in input().split(' ')])

primary_diagonal_sum = sum([matrix[i][i] for i in range(rows)])
secondery_diagonal_sum = sum([matrix[i][-i-1] for i in range(rows)])

abs_total_sum = abs(primary_diagonal_sum - secondery_diagonal_sum)
print(abs_total_sum)