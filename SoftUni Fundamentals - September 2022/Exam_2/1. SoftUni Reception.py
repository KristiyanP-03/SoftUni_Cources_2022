worker1s_students = int(input())
worker2s_students = int(input())
worker3s_students = int(input())
students_count = int(input())
hours_counter = 0
answers_per_hour = worker1s_students + worker2s_students + worker3s_students
while True:
    if students_count > 0:
        hours_counter += 1
        if hours_counter % 4 == 0:
            continue
        students_count -= answers_per_hour
    elif students_count <= 0:
        students_count = 0
        break
print(f"Time needed: {hours_counter}h.")

