string_of_random_symbols = input()
character = ""
number = ""
symbol = ""

for element in string_of_random_symbols:
    if element.isalpha():
        character += element
    elif element.isdigit():
        number += element
    else:
        symbol += element
print(number)
print(character)
print(symbol)