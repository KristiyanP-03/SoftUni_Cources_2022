import re

dates = input()
date_format = r'(\d{2})([\/.-])([A-Z][a-z]{2})\2([0-9]{4})\b'
formating = re.findall(date_format, dates)
for match in formating:
    print(f'Day: {match[0]}, Month: {match[2]}, Year: {match[3]}')