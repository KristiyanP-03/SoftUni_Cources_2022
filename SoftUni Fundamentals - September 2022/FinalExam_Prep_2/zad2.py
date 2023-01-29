import re
pair = 0
connect_str = ""
mirror_words = []
have_mirror_words = False

data = input()
pattern = r"(#|@)[A-Za-z]{3,}(\1)(#|@)[A-Za-z]{3,}(\1)"
matches = re.finditer(pattern, data)

for match in matches:
    current_math_1 = match.group()
    print(current_math_1)
    current_math_2 = match.group()
    print(current_math_2)
    current_math_1 = re.split('#|@', match.group())
    print(current_math_1)
    current_math_2 = re.split('#|@', match.group())
    print(current_math_2)
    current_math_1 = re.split('#|@', match.group())[1]
    print(current_math_1)
    current_math_2 = re.split('#|@', match.group())[3]
    print(current_math_2)
    pair += 1
    if current_math_1 == current_math_2[::-1]:
        have_mirror_words = True
        connect_str = f"{current_math_1} <=> {current_math_2}"
        mirror_words.append(connect_str)
        connect_str = ""
    print(mirror_words)

if pair == 0:
    print("No word pairs found!")
else:
    print(f"{pair} word pairs found!")

if have_mirror_words:
    print("The mirror words are:")
    print(", ".join(mirror_words))
else:
    print("No mirror words!")

