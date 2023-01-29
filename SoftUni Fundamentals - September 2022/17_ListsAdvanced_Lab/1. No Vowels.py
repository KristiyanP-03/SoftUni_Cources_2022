text = input()
banned_chars = ["a", "o", "u", "e", "i"]
new_text = "".join([char for char in text if char.lower() not in banned_chars])
print(new_text)