string = input()
new_string = ""
for index, char in enumerate(string):
    if char not in new_string or string[index - 1]  != char:
        new_string += char
print(new_string)