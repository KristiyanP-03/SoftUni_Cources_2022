storage = {}
while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    if resource not in storage:
        storage[resource] = quantity
    else:
        storage[resource] += quantity
for resources_in_storage, quantity_of_the_current_resorce in storage.items():
    print(f"{resources_in_storage} -> {quantity_of_the_current_resorce}")