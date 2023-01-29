students_dict = {}
command = input()
while ":" in command:
    student_name, student_id, course = command.split(":")

    if course not in students_dict:
        students_dict[course] = {}
    students_dict[course][student_id] = student_name
    command = input()

command = " ".join(command.split("_"))

for key, value in students_dict.items():
    if key == command:
        for student_id, student_name in value.items():
            print(f'{student_name} - {student_id}')

