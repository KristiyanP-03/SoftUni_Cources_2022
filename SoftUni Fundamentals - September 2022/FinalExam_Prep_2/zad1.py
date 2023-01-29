message = input()

while True:
    command_line = input()

    if command_line == "Reveal":
        break

    command_line = command_line.split(":|:")
    command = command_line[0]

    if command == "InsertSpace":
        index = int(command_line[1])
        message = message[:index] + " " + message[index:]
        print(message)

    elif command == "Reverse":
        substring = command_line[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            substring = substring[::-1]
            message = message + substring
            print(message)
        else:
            print("error")

    elif command == "ChangeAll":
        substring, replacement = command_line[1], command_line[2]
        while substring in message:
            message = message.replace(substring, replacement)
        print(message)

print(f"You have a new text message: {message}")

