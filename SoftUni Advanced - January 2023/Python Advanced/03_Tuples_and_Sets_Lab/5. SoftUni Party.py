reserved_places = int(input())

reserved_regular_set = set()
reserved_vip_set = set()

for invite in range(reserved_places):
    invitation_key = input()
    if invitation_key[0].isdigit():
        reserved_vip_set.add(invitation_key)
    else:
        reserved_regular_set.add(invitation_key)

while True:
    arived_key = input()
    if arived_key == "END":
        break
    if arived_key in reserved_vip_set:
        reserved_vip_set.remove(arived_key)
    elif arived_key in reserved_regular_set:
        reserved_regular_set.remove(arived_key)


vip_list = []
for vip in reserved_vip_set:
    vip_list.append(vip)
vip_list = sorted(vip_list)

regular_list = []
for regular in reserved_regular_set:
    regular_list.append(regular)
regular_list = sorted(regular_list)

print_counter = len(vip_list) + len(regular_list)

print(print_counter)
for invite in vip_list:
    print(invite)
for invite in regular_list:
    print(invite)