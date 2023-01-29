storage = {}
products_counter = 0
quantity_counter = 0
while True:
    command = input()
    if command == "statistics":
        print("Products in stock:")
        for dict_key, dict_value in storage.items():
            print(f"- {dict_key}: {dict_value}")
            products_counter += 1
            quantity_counter += int(dict_value)
        print(f"Total Products: {products_counter}")
        print(f"Total Quantity: {quantity_counter}")
        break
    key , value = command.split(": ")
    if key in storage.keys():
        storage[key] += int(value)
    else:
        storage[key] = int(value)