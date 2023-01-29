people = int(input())
str_lifts_in_list = input().split(" ")
lifts_in_list = []
flag_empty_spot = False
flag_no_more_space = False

for slot in str_lifts_in_list:
    slot = int(slot)
    while slot != 4:
        if people == 0:
            break
        slot += 1
        people -= 1
    lifts_in_list.append(slot)
if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    lifts_in_str = []
    lifts_in_str = [str(slot) for slot in lifts_in_list]
    final_list = " ".join(lifts_in_str)
    print(final_list)
elif people == 0:
    for slot_taken in lifts_in_list:
        if slot_taken != 4:
            flag_empty_spot = True
            break
    else:
        flag_no_more_space
if flag_empty_spot:
    print("The lift has empty spots!")
    lifts_in_str = []
    lifts_in_str = [str(slot) for slot in lifts_in_list]
    final_list = " ".join(lifts_in_str)
    print(final_list)
elif flag_no_more_space:
    lifts_in_str = []
    lifts_in_str = [str(slot) for slot in lifts_in_list]
    final_list = " ".join(lifts_in_str)
    print(final_list)

