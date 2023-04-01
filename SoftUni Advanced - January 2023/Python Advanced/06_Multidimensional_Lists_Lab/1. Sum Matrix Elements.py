rows, cols = input().split(", ")
rows = int(rows)
matrix = []
sum_of_matrix_numbers = 0

for row in range(rows):
    matrix_row_content = list(map(int, input().split(", ")))
    matrix.append(matrix_row_content)

    for number in matrix_row_content:
        sum_of_matrix_numbers += number

print(sum_of_matrix_numbers)
print(matrix)

