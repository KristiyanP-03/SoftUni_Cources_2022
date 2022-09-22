characters = int(input())
for i in range(characters):
    for j in range(characters):
        for g in range(characters):
            print(chr(i + 97), end="")
            print(chr(j + 97), end="")
            print(chr(g + 97))