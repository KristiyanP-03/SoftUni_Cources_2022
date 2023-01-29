from _collections import deque

player = input().split(" ")
potato_toss = int(input())
queue = deque(player)

while len(queue) > 1:
    for _ in range(potato_toss - 1):
        queue.append(queue.popleft())

    print(f"Removed {queue.popleft()}")
print(f"Last is {queue[0]}")