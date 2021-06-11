import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

queue = deque()
save_queue = list()

for i in range(1, N + 1):
    queue.append(i)

while queue:
    for count in range(K):
        cache = queue.popleft()
        if count == K - 1:
            save_queue.append(cache)
            break
        queue.append(cache)
print('<', end = '')
for i in range(len(save_queue)):
    if i == len(save_queue) - 1:
        print(save_queue[i], end = '')
    else:
        print(save_queue[i], end = ', ')
print('>')