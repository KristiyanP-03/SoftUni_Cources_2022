rows = int(input())
matrix = []
sum_of_elemen_on_diagonal = 0

for row in range(rows):
    matrix.append([int(x) for x in input().split()])

for index in range(len(matrix)):
    sum_of_elemen_on_diagonal += matrix[index][index]

print(sum_of_elemen_on_diagonal)