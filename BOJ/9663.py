import sys
from collections import deque

N = int(sys.stdin.readline())

maps = [[False for _ in range(N)] for _ in range(N)]
count = 0

def func (y):
    if y >= N:
        count += 1
        return
    
    for x in range(N):
   
        maps[y][x] = True
        if x == dy:                             # 세로로 같을 때
                continue
        elif dx - dy == x - y:                  # 대각선 1
                continue
        elif dx + dy == x + y:                  # 대각선 2
                continue
        else:
    


'''for i in range(N * N):
    x = i % N
    y = int(i / N)

    for dx in range(N):
        if x == dx:                                 # 가로로 같을 때
            continue                         
        for dy in range(N):
            if y == dy:                             # 세로로 같을 때
                continue
            elif dx - dy == x - y:                  # 대각선 1
                continue
            elif dx + dy == x + y:                  # 대각선 2
                continue
            else:
                cache = dy * N + dx
                cache_array = [i , cache]
                cache_array.sort()
                if cache_array not in queue:
                    queue.append(cache_array)
    print(len(queue))'''
