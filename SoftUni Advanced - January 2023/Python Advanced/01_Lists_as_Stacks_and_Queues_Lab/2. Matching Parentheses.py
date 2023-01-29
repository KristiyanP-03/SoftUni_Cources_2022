math_problem = input()
stack = []

for i in range(len(math_problem)):
    char = math_problem[i]
    if char == "(":
        stack.append(i)
    elif char == ")":
        start = stack.pop()
        print(math_problem[start:i + 1:])