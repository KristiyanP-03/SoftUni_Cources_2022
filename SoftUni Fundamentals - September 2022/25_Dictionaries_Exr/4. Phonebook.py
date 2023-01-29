phonebook = {}
while True:
    entry = input()
    if "-" not in entry:
        n = int(entry)
        break
    contact, phone_number = entry.split("-")
    phonebook[contact] = phone_number

for i in range(n):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")