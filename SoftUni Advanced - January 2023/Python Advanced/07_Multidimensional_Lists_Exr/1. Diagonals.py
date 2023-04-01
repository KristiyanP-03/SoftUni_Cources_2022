rows = int(input())
matrix = []

for i in range(rows):
    row = input().split(", ")
    matrix.append(row)

primary_diagonal = [matrix[i][i] for i in range(rows)]
secondary_diagonal = [matrix[i][rows-i-1] for i in range(rows)]

primary_diagonal_sum = sum([int(x) for x in primary_diagonal])
secondary_diagonal_sum = sum([int(x) for x in secondary_diagonal])

print(f"Primary diagonal: {', '.join(primary_diagonal)}. Sum: {primary_diagonal_sum}")
print(f"Secondary diagonal: {', '.join(secondary_diagonal)}. Sum: {secondary_diagonal_sum}")
