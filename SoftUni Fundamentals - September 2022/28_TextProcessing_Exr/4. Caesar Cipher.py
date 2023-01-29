string = input()
encrypted_version = ""
for char in string:
    char = ord(char) + 3
    char = chr(char)
    encrypted_version += char
print(encrypted_version)