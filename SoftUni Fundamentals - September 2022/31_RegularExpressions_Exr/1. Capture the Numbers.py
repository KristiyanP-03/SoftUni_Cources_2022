import re

digit_finder = r"\d+"

data = input()
while data:

    found = re.findall(digit_finder, data)
    if found:
        print(" ".join(found), end=" ")
    data = input()
