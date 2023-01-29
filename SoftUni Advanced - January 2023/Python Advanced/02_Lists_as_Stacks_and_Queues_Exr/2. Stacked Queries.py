stack = []
an_intiger = int(input())

for iteration in range (an_intiger):
    command_line = input()
    if command_line[0] == '1':
        number = int(command_line[2::])
        stack.append(number)
    elif command_line == "2":
        if stack:
            stack.pop()
    elif command_line == "3":
        print(max(stack))
    elif command_line == "4":
        print(min(stack))
stack.reverse()
print(', '.join(map(str, stack)))