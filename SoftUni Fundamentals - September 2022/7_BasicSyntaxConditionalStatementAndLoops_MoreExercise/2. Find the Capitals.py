string = input()
list_of_uppercases = []
for i, v in enumerate(string):
    if v.isupper():
        list_of_uppercases.append(i)
    elif v.islower():
        continue
print(list_of_uppercases)