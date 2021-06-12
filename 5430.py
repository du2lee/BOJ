import sys
from collections import deque

boolean = True
T = int(sys.stdin.readline())

for _ in range(T):
    count = 0
    p = deque(input())
    N = int(sys.stdin.readline())
    
    cache = input()
    cache = cache.lstrip('[')
    cache = cache.rstrip(']')
    if len(cache) > 0:
        queue = deque(cache.split(','))
    else:
        boolean = False
        queue = deque()

    while p:
        boolean = True
        cache = p.popleft()

        if cache == 'R':
            count += 1
        elif cache == 'D':
            if len(queue) <= 0:
                boolean = False
                break
            if count % 2 == 0:
                queue.popleft()
            else:
                queue.pop()

    if count % 2 == 1:
        queue.reverse()

    if boolean == False:
        print("error")
    else:
        last = queue.pop()
        print('[', end = '')
        while queue:
            print(queue.popleft()+',', end = '')
        print(last, end='')
        print(']')