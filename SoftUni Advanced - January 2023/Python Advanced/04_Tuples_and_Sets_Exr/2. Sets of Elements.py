number_of_inputs_in_set1, number_of_inputs_in_set2 = map(int, input().split(" "))
set1 = set()
set2 = set()

for current_input in range(number_of_inputs_in_set1):
    number = int(input())
    set1.add(number)
set2 = {int(input()) for _ in range(number_of_inputs_in_set2)}

print(*set1.intersection(set2), sep="\n")