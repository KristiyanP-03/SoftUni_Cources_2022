tank = 255
total_took = 0
pour = int(input())
for i in range(pour):
    take = int(input())
    if total_took + take > tank:
        print("Insufficient capacity!")
        i += 1
        continue
    total_took += take
print(total_took)