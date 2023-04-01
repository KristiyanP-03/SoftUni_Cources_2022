from collections import deque

chocolate_ingredients = [int(value) for value in input().split(", ")]
stack_milk_cups = deque([int(value) for value in input().split(", ")])

milkshakes = 0
job_well_done = False

while chocolate_ingredients and stack_milk_cups:

    current_chocolate_ingredient = chocolate_ingredients.pop()
    current_milk_cup = stack_milk_cups.popleft()

    if (current_milk_cup > 0) == (current_chocolate_ingredient > 0):
        milkshakes += 1
    elif (current_milk_cup > 0) != (current_chocolate_ingredient > 0):
        current_chocolate_ingredient -= 5
        stack_milk_cups.append(current_milk_cup)
    else:
        if current_chocolate_ingredient <= 0:
            pass
        if current_milk_cup <= 0:
            pass

    if milkshakes == 5:
        job_well_done = True
        break

if job_well_done:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate_ingredients:
    print(f"Chocolate: {', '.join([str(i) for i in chocolate_ingredients])}")
else:
    print("Chocolate: empty")
if stack_milk_cups:
    print(f"Milk: {', '.join([str(i) for i in stack_milk_cups])}")
else:
    print("Milk: empty")

