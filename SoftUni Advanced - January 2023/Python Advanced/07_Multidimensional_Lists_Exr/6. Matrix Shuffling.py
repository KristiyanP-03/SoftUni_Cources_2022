rows, columns = list(map(int, input().split()))

matrix = [input().split() for row in range(rows)]

command = input()
while command != "END":
    if len(command.split()) == 5:
        swap = command.split()

        if swap[0] == "swap" and ''.join(swap[1:]).isdigit():
            row1, col1, row2, col2 = int(swap[1]), int(swap[2]), int(swap[3]), int(swap[4])

            if row1 < rows and row2 < rows and col1 < columns and col2 < columns:
                matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
                [print(' '.join(row)) for row in matrix]

            else:
                print("Invalid input!")

        else:
            print("Invalid input!")

    else:
        print("Invalid input!")

    command = input()