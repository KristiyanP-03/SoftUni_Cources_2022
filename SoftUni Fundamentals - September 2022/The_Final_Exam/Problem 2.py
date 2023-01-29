import re

hiden_eggs = input()
pattern = r"[@|#]+([a-z]{3,})[@|#]+([^A-Za-z0-9]+)?[\/]{1,}([0-9]+)[\/]{1,}"
matches = re.findall(pattern, hiden_eggs)

for match in matches:
    color, amount = match[0], match[2]
    print(f"You found {amount} {color} eggs!")