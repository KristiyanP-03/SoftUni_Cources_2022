from collections import deque

delivery_box = deque(map(int, input().split(" ")))
rack = int(input())
slots_in_wardrobe = 1

current_rack = 0
while delivery_box:
    if delivery_box[0] + current_rack <= rack:
        current_rack += delivery_box[0]
        delivery_box.popleft()
    else:
        slots_in_wardrobe += 1
        current_rack = 0

print(slots_in_wardrobe)