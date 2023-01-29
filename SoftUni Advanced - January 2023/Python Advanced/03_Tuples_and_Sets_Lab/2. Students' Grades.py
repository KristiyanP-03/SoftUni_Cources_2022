number_of_inputs = int(input())
book = {}

for _ in range(number_of_inputs):
    name, grade = input().split(" ")
    if name not in book.keys():
        book[name] = []
    book[name].append(float(grade))

for name, grades in book.items():
    avg_grade = sum(grades) / len(grades)
    str_grade = " ".join(map(lambda grade: f"{grade:.2f}", grades))
    print(f"{name} -> {str_grade} (avg: {avg_grade:.2f})")
