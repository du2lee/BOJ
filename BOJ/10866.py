import sys
from collections import deque

N = int(sys.stdin.readline())
Deques = deque()

for _ in range(N):
    cache = deque(sys.stdin.readline().split())
    if cache[0] == 'push_front':
        Deques.appendleft(cache[1])
    elif cache[0] == 'push_back':
        Deques.append(cache[1])
    elif cache[0] == 'pop_front':
        if len(Deques) <= 0:
            print(-1)
        else:
            print(Deques.popleft())
    elif cache[0] == 'pop_back': 
        if len(Deques) <= 0:
            print(-1)
        else:
            print(Deques.pop())
    elif cache[0] == 'size': 
        print(len(Deques))
    elif cache[0] == 'empty': 
        if len(Deques) <= 0:
            print(1)
        else:
            print(0)
    elif cache[0] == 'front': 
        if len(Deques) <= 0:
            print(-1)
        else:
            print(Deques[0])
    elif cache[0] == 'back': 
        if len(Deques) <= 0:
            print(-1)
        else:
            print(Deques[-1])