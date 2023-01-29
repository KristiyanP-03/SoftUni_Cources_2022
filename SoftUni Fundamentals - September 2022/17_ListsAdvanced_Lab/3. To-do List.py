list_with_all_tasks = []
while True:
    note = input()
    if note == "End":
        break
    note_to_list = note.split("-")
    priority = int(note_to_list[0])
    task = note_to_list[1]
    list_with_all_tasks.append([priority, task])
    to_do_list = [task_info[1] for task_info in sorted(list_with_all_tasks)]
print(to_do_list)
