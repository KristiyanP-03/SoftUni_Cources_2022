stack_of_nums = input().split()
reversed_stack = []
while stack_of_nums:
    reversed_stack.append(stack_of_nums.pop())
print(' '.join(reversed_stack))