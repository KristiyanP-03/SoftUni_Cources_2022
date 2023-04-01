first_sequence_of_int = set([int(num) for num in input().split(" ")])
second_sequence_of_int = set([int(num) for num in input().split(" ")])

def union_funct(your_set, second_set):
    your_set = your_set.union(second_set)
    return your_set
def difference_funct(your_set, second_set):
    your_set = your_set.difference(second_set)
    return your_set


for _ in range(int(input())):
    command = input()

    if "Add First" in command:
        command, pointer, *set_to_add = command.split(" ")
        set_to_add = set([int(num) for num in set_to_add])
        first_sequence_of_int = union_funct(first_sequence_of_int, set_to_add)

    elif "Add Second" in command:
        command, pointer, *set_to_add = command.split(" ")
        set_to_add = set([int(num) for num in set_to_add])
        second_sequence_of_int = union_funct(second_sequence_of_int, set_to_add)

    elif "Remove First" in command:
        command, pointer, *set_to_remove = command.split(" ")
        set_to_remove = set([int(num) for num in set_to_remove])
        first_sequence_of_int = difference_funct(first_sequence_of_int, set_to_remove)

    elif "Remove Second" in command:
        command, pointer, *set_to_remove = command.split(" ")
        set_to_remove = set([int(num) for num in set_to_remove])
        second_sequence_of_int = difference_funct(second_sequence_of_int, set_to_remove)

    elif command == "Check Subset":
        if(first_sequence_of_int.issubset(second_sequence_of_int) == True \
                or second_sequence_of_int.issubset(first_sequence_of_int)) == True:
            print("True")
        else:
            print("False")

print(", ".join([str(num) for num in sorted(first_sequence_of_int)]))
print(", ".join([str(num) for num in sorted(second_sequence_of_int)]))
