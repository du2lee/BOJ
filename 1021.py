import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())

queue = deque(map(int, sys.stdin.readline().split()))
save_queue = deque()
result_queue = deque()
count = 0

for i in range(1, N + 1):
    save_queue.append(i)

for i in queue:
    idx = save_queue.index(i)
    if i == save_queue[0]:
        save_queue.popleft()
    elif idx <= int(len(save_queue) / 2):
        for _ in range(idx):
            save_queue.append(save_queue.popleft())
            count += 1
        save_queue.popleft()
    elif idx > int(len(save_queue) / 2):
        for _ in range(len(save_queue), idx, -1):
            save_queue.appendleft(save_queue.pop())
            count += 1
        save_queue.popleft()
print(count)

