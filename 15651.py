import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
array = deque()

def func():
    if  len(array) == M:
        print(*array)
        return

    for i in range(1 , N+1):
        array.append(i)
        func()
        array.pop()

func()