import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N , a= map(int, sys.stdin.readline().split())
    inputs = deque(map(int, sys.stdin.readline().split()))
    queue = deque()
    count = 0
    for i in range(len(inputs)):
        if i == a:
            queue.append([inputs.popleft(), 1])
        else:
            queue.append([inputs.popleft(), 0])
    while queue:
        cache = queue.popleft()
        boolean = True
        for i in queue:
            if i[0] > cache[0]:
                queue.append(cache)
                boolean = False
                break
        if boolean == True:
            count += 1
            if cache[1] == 1:
                print(count)
                break