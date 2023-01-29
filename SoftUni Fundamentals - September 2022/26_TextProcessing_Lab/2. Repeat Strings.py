list_of_strings = input().split(" ")
for string in list_of_strings:
    print(string * len(string), end="")