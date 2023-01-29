import re

data = input()
pattern = r"\b_([A-Za-z0-9]+)\b"
special_words = re.findall(pattern, data)
print(",".join(special_words))