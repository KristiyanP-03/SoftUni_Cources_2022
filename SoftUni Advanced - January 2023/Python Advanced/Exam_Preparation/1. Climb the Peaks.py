from collections import deque

Mountain_Peaks_Difficulty_level = {
    "Vihren": 80, "Kutelo": 90, "Banski Suhodol": 100, "Polezhan": 60, "Kamenitza": 70 }

daily_food = [int(meal) for meal in input().split(", ")]
daily_stamina = deque([int(stamina_power) for stamina_power in input().split(", ")])

conquered_peaks = []
for peak, difficulty in Mountain_Peaks_Difficulty_level.items():

    if daily_food and daily_stamina:

        if (daily_food[-1] + daily_stamina[0]) >= difficulty:
            conquered_peaks.append(peak)
            daily_food.pop()
            daily_stamina.popleft()


        else:
            while daily_food and daily_stamina:

                if (daily_food[-1] + daily_stamina[0]) < difficulty:
                    daily_food.pop()
                    daily_stamina.popleft()

                else:
                    conquered_peaks.append(peak)
                    daily_food.pop()
                    daily_stamina.popleft()
                    break

    else:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        if conquered_peaks:
            print("Conquered peaks:")
            print('\n'.join(conquered_peaks))
        break

else:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
    print("Conquered peaks:")
    print('\n'.join(conquered_peaks))