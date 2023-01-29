list_with_strings = input().split(" ")
list_with_chars = []
for word in list_with_strings:
    for character in word:
        list_with_chars.append(character)
dict_with_chars_occurrences = {}
for char in list_with_chars:
    if char not in dict_with_chars_occurrences:
        dict_with_chars_occurrences[char] = 1
    else:
        dict_with_chars_occurrences[char] += 1
for the_charcter, the_occurrence in dict_with_chars_occurrences.items():
    print(f"{the_charcter} -> {the_occurrence}")