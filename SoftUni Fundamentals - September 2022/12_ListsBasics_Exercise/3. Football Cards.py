string_of_send_off_players = input()
list_of_send_off_players = string_of_send_off_players.split(" ")
list_team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7","A-8","A-9", "A-10", "A-11"]
list_team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7","B-8","B-9", "B-10", "B-11"]
for send_off_player in list_of_send_off_players:
    if send_off_player in list_team_a:
        list_team_a.remove(send_off_player)
    elif send_off_player in list_team_b:
        list_team_b.remove(send_off_player)
    if len(list_team_a) < 7:
        print(f"Team A - {len(list_team_a)}; Team B - {len(list_team_b)}")
        print("Game was terminated")
        break
    elif len(list_team_b) < 7:
        print(f"Team A - {len(list_team_a)}; Team B - {len(list_team_b)}")
        print("Game was terminated")
        break
else:
    print(f"Team A - {len(list_team_a)}; Team B - {len(list_team_b)}")
