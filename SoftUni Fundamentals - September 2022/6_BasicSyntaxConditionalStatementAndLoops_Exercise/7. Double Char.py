while True:
    word = input()
    if word == "End":
        break
    if word == "SoftUni":
        continue
    new_word = ""
    for i in range(len(word)):
        new_word += 2 * word[i]
    print(new_word)