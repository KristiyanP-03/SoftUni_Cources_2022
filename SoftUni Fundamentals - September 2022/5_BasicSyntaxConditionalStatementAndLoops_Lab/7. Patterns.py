num = int(input())
for r in range(1, num + 1, 1):
    for c in range(0, r):
        print("*", end="")
    print()
for i in range(num - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        print("*", end="")
    print()