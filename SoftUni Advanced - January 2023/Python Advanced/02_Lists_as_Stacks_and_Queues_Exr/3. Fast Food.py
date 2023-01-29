from _collections import deque

food_supplies = int(input())
queue = deque(map(int, input().split()))

print(max(queue))

while queue:
    if food_supplies - queue[0] >= 0:
        food_supplies -= queue[0]
        queue.popleft()
    else:
        str_queue = ' '.join(map(str, queue))
        print(f"Orders left: {str_queue}")
        break
else:
    print("Orders complete")