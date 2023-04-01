from collections import deque

textiles = deque([int(x) for x in input().split(' ')])
medicaments = [int(x) for x in input().split(' ')]

Patch = 30
Bandage	= 40
MedKit = 100
crafted_Patch = 0
crafted_Bandage	= 0
crafted_MedKit = 0

parts_left = 0
while textiles and medicaments:

    if (textiles[0] + medicaments[-1]) > MedKit:
        crafted_MedKit += 1
        parts_left = (textiles[0] + medicaments[-1])- 100
        textiles.popleft()
        medicaments.pop()
        medicaments[-1] += parts_left

    elif (textiles[0] + medicaments[-1]) == MedKit:
        crafted_MedKit += 1
        textiles.popleft()
        medicaments.pop()

    elif (textiles[0] + medicaments[-1]) == Bandage:
        crafted_Bandage += 1
        textiles.popleft()
        medicaments.pop()

    elif (textiles[0] + medicaments[-1]) == Patch:
        crafted_Patch += 1
        textiles.popleft()
        medicaments.pop()

    else:
        textiles.popleft()
        medicaments[-1] += 10


item_storting_dict = {"Patch": crafted_Patch, "Bandage": crafted_Bandage, "MedKit": crafted_MedKit}

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")

    sorted_items = sorted(item_storting_dict.items(), key=lambda x: (-x[1], x[0]))
    for key, value in sorted_items:
        if value:
            print(f"{key} - {value}")

elif not textiles:
    print("Textiles are empty.")
    sorted_items = sorted(item_storting_dict.items(), key=lambda x: (-x[1], x[0]))
    for key, value in sorted_items:
        if value:
            print(f"{key} - {value}")

    print(f"Medicaments left: {', '.join(reversed([str(x) for x in medicaments]))}")

elif not medicaments:
    print("Medicaments are empty.")
    sorted_items = sorted(item_storting_dict.items(), key=lambda x: (-x[1], x[0]))
    for key, value in sorted_items:
        if value:
            print(f"{key} - {value}")

    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
