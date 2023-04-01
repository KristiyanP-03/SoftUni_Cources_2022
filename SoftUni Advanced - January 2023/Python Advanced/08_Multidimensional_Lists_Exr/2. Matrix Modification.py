rows = int(input())

matrix = [
    [int(num) for num in input().split()]
    for row in range(rows)
]

command = input()
while command != "END":
    try:

        operation, row, col, value = command.split()
        row, col, value = int(row), int(col), int(value)

        if row >= 0 and col >= 0:

            if operation == "Add":
                matrix[row][col] += value

            elif operation == "Subtract":
                matrix[row][col] -= value

        else:
            print("Invalid coordinates")

        command = input()

    except Exception:
        print("Invalid coordinates")
        command = input()

[print(" ".join([str(num) for num in line])) for line in matrix]
