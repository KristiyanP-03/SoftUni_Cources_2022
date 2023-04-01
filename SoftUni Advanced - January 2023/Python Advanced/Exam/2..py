n, m = map(int, input().split())

playground = []
for _ in range(n):
    playground.append(input().split())

nested_list = [[i, playground[i].index('B')] for i in range(len(playground)) if 'B' in playground[i]]
player_position = nested_list[0]
playground[player_position[0]][player_position[1]] = '-'

moves_made = 0
touched_opponents = 0

while True:
    command = input()
    if command == 'Finish':
        break

    if command == "left":
        if playground[player_position[0]][player_position[1] - 1] == 'O' or player_position[1] - 1 == -1:
            continue
        player_position[1] -= 1

    elif command == "right":
        try:
            if playground[player_position[0]][player_position[1] + 1] == 'O':
                continue
            player_position[1] += 1
        except IndexError:
            continue

    elif command == "up":
        if playground[player_position[0] - 1][player_position[1]] == 'O' or player_position[0] - 1 == -1:
            continue
        player_position[0] -= 1

    elif command == "down":
        try:
            if playground[player_position[0] + 1][player_position[1]] == 'O':
                continue
            player_position[0] += 1
        except IndexError:
            continue


    if playground[player_position[0]][player_position[1]] == 'P':
        touched_opponents += 1
        moves_made += 1
        playground[player_position[0]][player_position[1]] = '-'

    elif playground[player_position[0]][player_position[1]] == '-':
        moves_made += 1

    if touched_opponents == 3:
        break

print('Game over!')
print(f'Touched opponents: {touched_opponents} Moves made: {moves_made}')