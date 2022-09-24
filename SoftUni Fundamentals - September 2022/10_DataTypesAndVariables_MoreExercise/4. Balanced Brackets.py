n_lines = int(input())
balanced = False
opening_bracket = 0
closing_bracket = 0
for line in range(n_lines):
    char = input()
    if char == "(":
        opening_bracket += 1
    elif char == ")":
        closing_bracket += 1
    if opening_bracket == 2 and closing_bracket == 0 or opening_bracket == 0 and closing_bracket == 1:
        break
else:
    balanced = True
if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
