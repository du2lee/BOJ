import sys
from collections import deque

N = int(sys.stdin.readline())
count = 0
queue = deque()

for i in range(1, N + 1):
    queue.append(i)


while len(queue) > 1:
    if count % 2 == 0:
        queue.popleft()

    else:
        cache = queue.popleft()
        queue.append(cache)
    count += 1

print(queue.pop())