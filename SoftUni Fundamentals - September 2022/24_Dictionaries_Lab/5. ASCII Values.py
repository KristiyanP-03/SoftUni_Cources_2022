list_of_characters = input().split(", ")
dict_with_chars_and_their_values = {char:ord(char) for char in list_of_characters}
print(dict_with_chars_and_their_values)