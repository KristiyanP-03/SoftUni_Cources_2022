n = input()
stack_S = []

for i in range(int(n), 0, -1):
    stack_S.append(i)

stack_P = stack_S.copy()
stack_P.reverse()

while stack_S:
    print(stack_S.pop(), end=" ")
print()

while stack_P:
    print(stack_P.pop(), end=" ")
