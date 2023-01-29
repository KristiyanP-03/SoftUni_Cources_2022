from _collections import deque

expression = input()
opening_braket = "({["
closing_braket = ")}]"
types_of_parentheses = {"(": ")", "{": "}", "[": "]"}

expression_list = deque([])
stack_checker = []

for bracket in expression:
    expression_list.append(bracket)

while expression_list:
    current_bracket = expression_list[0]
    if current_bracket in opening_braket:
        stack_checker.append(expression_list.popleft())
    elif current_bracket in closing_braket:
        last_opening_bracket = stack_checker.pop()
        if types_of_parentheses[last_opening_bracket] == current_bracket:
            expression_list.popleft()
            continue
        else:
            print("NO")
            break
else:
    print("YES")