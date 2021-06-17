import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
array = list()

def func(m):
    if  len(array) == M:
        print(*array)
        return

    for i in range(m , N+1):
        if i not in array:
            array.append(i)
            func(i + 1)
            array.pop()

func(1)