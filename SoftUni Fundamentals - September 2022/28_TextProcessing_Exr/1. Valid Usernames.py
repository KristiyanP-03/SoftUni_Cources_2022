list_of_usernames = input().split(", ")
for username in list_of_usernames:
    if 3 <= len(username) <= 16:
        for char in username:
            if char.isdigit() or char.isalpha() or  char == "-" or char == "_":
                pass
            else:
                break
        else:
            print(username)