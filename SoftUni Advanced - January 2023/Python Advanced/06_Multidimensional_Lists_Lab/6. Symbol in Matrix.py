rows = int(input())
matrix = []

for row in range(rows):
    matrix.append([char for char in input()])

target_char = input()
flag = False

for index in range(len(matrix)):
    for char in reversed(matrix[index]):
        if char == target_char:
            print(f"({index}, {matrix[index].index(char)})")
            flag = True

if not flag:
    print(f"{target_char} does not occur in the matrix")