import re

data = input()
email_pattern = r'\s(([a-z0-9]+[a-z0-9\.\-\_]*)@[a-z\-]+(\.[a-z]+)+)\b'
match = re.findall(email_pattern, data)
for email in match:
    print(email[0])
