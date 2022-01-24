import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
check = [False] * N
array = deque()

def func(m):
    if  m == M:
        print(*array)
        return

    for i in range(N):
        if check[i] != True:
            check[i] = True
            array.append(i + 1)
            func(m + 1)
            check[i] = False
            array.pop()

func(0)