import sys
from collections import deque
from math import sqrt

if __name__ == "__main__":

    M = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    array = deque()
    sum = 0
    for i in range(1, 10000):
        if i ** 2 >= M and i ** 2 <= N:
            sum += i * i
            array.append(i * i)
    if len(array) == 0:
        print(-1)
    else:
        print(sum)
        print(min(array))