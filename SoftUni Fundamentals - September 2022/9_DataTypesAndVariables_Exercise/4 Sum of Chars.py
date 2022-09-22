n = int(input())
total_sum = 0
for i in range(n):
    char = input()
    total_sum += ord(char)
print("The sum equals: " + str(total_sum))