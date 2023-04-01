def get_info(name, town, age):
    return f"This is {name} from {town} and he is {age} years old"

person = {"name": "Kris", "town": "Varna", "age": 18}
print(get_info(**person))