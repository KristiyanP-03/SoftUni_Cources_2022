rows = int(input())
racing_number = input()
matrix = []

for row in range(rows):
    matrix.append([race_route for race_route in input().split(' ')])

car_position = [0, 0]
distance_counter = 0
tunel_entrence, tunel_exit = [[i, matrix[i].index('T')] for i in range(len(matrix)) if 'T' in matrix[i]]

while True:

    command = input()
    if command == "End":
        print(f"Racing car {racing_number} DNF.")
        break


    if command == "left":
        car_position[1] -= 1


    elif command == "right":
        car_position[1] += 1


    elif command == "up":
        car_position[0] -= 1


    elif command == "down":
        car_position[0] += 1


    if matrix[car_position[0]][car_position[1]] == 'T':

        distance_counter += 30
        if car_position == tunel_entrence:
            car_position = tunel_exit
            matrix[tunel_entrence[0]][tunel_entrence[1]] = '.'
            matrix[tunel_exit[0]][tunel_exit[1]] = '.'

        elif car_position == tunel_exit:
            car_position = tunel_entrence
            matrix[tunel_entrence[0], tunel_entrence[1]] = '.'
            matrix[tunel_exit[0]][tunel_exit[1]] = '.'
        continue

    distance_counter += 10

    if matrix[car_position[0]][car_position[1]] == 'F':
        print(f"Racing car {racing_number} finished the stage!")
        break


print(f"Distance covered {distance_counter} km." )

matrix[car_position[0]][car_position[1]] = 'C'
for lst in matrix:
    print(''.join(lst))