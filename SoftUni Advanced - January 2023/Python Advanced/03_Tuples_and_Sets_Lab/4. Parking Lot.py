number_of_events = int(input())

parking_lot = set()

def enetring_car(car_number, parking):
    parking.add(car_number)
    return parking;
def exiting_car(car_number, parking):
    parking.remove(car_number)
    return parking;

for _ in range(number_of_events):
    action, car_plate = input().split(", ")
    if action == "IN":
        enetring_car(car_plate, parking_lot)
    elif action == "OUT":
        if car_plate in parking_lot:
            exiting_car(car_plate, parking_lot)

flag = False
for plate in parking_lot:
    print(plate)
    flag = True

if not flag:
    print("Parking Lot is Empty")
