course = input()

while True:
    command = input()
    if command == "Travel":
        break
    elif "Add Stop:" in command:
        command, index, string = command.split(":")
        index = int(index)
        course = course[:index] + string + course[index:]
    elif "Remove Stop:" in command:
        command, start, end = command.split(":")
        start = int(start)
        end = int(end)
        course = course[:start] + course[end+1:]
    elif "Switch:" in command:
        command, old_string, new_string = command.split(":")
        course = course.replace(old_string, new_string)
    print(course)

print(f"Ready for world tour! Planned stops: {course}")