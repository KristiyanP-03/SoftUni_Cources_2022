word = input()
reversed_word = ""
lenght = len(word)
for i in range(lenght - 1, -1, -1):
    reversed_word += word[i]
print(reversed_word)
