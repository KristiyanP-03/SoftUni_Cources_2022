dudes = int(input())
capcility = int(input())
courses = dudes // capcility
left_dudes = dudes % capcility
if left_dudes != 0:
    courses += 1
print(courses)