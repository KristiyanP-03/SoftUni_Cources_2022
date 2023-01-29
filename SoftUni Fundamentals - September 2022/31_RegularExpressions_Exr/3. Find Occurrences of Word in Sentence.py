import re

data = input()
data = data.lower()

special_word = input()
special_word = special_word.lower()
pattern = fr"\b{special_word}\b"

occurrences = re.findall(pattern, data)
print(len(occurrences))
