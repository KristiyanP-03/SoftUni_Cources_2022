import re
daily_cals = 2000
total_cal = 0
list_of_info = []

data = input()
pattern = r"(#|\|)([A-Za-z\s]+)(\1)([0-9]{2}/[0-9]{2}/[0-9]{2})(\1)([0-9]{1,4})(\1)"

matches = re.findall(pattern, data)

for match in matches:
    list_of_info.append([match[1], match[3], match[5]])
    total_cal += int(match[5])

days = total_cal // daily_cals

print(f"You have food to last you for: {days} days!")
for i in list_of_info:
    print(f"Item: {i[0]}, Best before: {i[1]}, Nutrition: {i[2]}")


