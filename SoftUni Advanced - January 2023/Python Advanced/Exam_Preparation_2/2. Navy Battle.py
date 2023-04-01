rows = int(input())
matrix = []

for row in range(rows):
    matrix.append([x for x in input()])

nested_list = [[i, matrix[i].index('S')] for i in range(len(matrix)) if 'S' in matrix[i]]
submarine_position = nested_list[0]
matrix[submarine_position[0]][submarine_position[1]] = '-'

mines = 3
flag_fail = False
battle_cruiser = 3
flag_win = False

while True:
    command = input()

    if command == "left":
        submarine_position[1] -= 1

    elif command == "right":
        submarine_position[1] += 1

    elif command == "up":
        submarine_position[0] -= 1

    elif command == "down":
        submarine_position[0] += 1


    if matrix[submarine_position[0]][submarine_position[1]] == '*':
        mines -= 1
        matrix[submarine_position[0]][submarine_position[1]] = '-'
        if mines == 0:
            flag_fail = True
            break

    elif matrix[submarine_position[0]][submarine_position[1]] == 'C':
        battle_cruiser -= 1
        matrix[submarine_position[0]][submarine_position[1]] = '-'
        if battle_cruiser == 0:
            flag_win = True
            break

matrix[submarine_position[0]][submarine_position[1]] = 'S'

if flag_fail:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_position[0]}, {submarine_position[1]}]!")
    for lst in matrix:
        print(''.join(lst))

elif flag_win:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
    for lst in matrix:
        print(''.join(lst))