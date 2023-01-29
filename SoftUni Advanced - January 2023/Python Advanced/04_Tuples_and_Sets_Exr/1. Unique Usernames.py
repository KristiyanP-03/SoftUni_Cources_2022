n_of_inputs = int(input())
usernames = set()

for _ in range(n_of_inputs):
    username = input()
    usernames.add(username)

for name in usernames:
    print(name)