days = int(input())
count_of_players = int(input())
group_energy = float(input())
no_energy = False

water = float(input())
total_water = days * count_of_players * water
water_day = 0
food = float(input())
total_food = days * count_of_players * food
food_day = 0

for day in range(1, days + 1):
    water_day += 1
    food_day += 1
    energy_lost = float(input())
    group_energy -= energy_lost
    if group_energy <= 0:
        no_energy = True
        break
    if water_day == 2:
        total_water -= total_water * 0.3
        group_energy += group_energy * 0.05
        water_day = 0
    if food_day == 3:
        total_food -= total_food / count_of_players
        group_energy += group_energy * 0.1
        food_day = 0
else:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")

if no_energy:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
