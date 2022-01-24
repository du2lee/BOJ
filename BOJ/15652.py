import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
array = deque()

def func():
    if  len(array) == M:
        print(*array)
        return

    for i in range(1 , N+1):
        if len(array) == 0:
            array.append(i)
            func()
            array.pop()
        else:
            if array[-1] <= i:
                array.append(i)
                func()
                array.pop()

func()