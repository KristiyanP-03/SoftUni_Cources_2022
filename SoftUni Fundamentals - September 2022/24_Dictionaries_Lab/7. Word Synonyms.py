n = int(input())
synonyms = {}

for i in range(n):
    word = input()
    sysnonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(sysnonym)
for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")