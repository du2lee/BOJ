import sys
from collections import deque

if __name__ == "__main__":
    array = deque()
    sum = 0
    for _ in range(7):
        inputs = int(sys.stdin.readline())
        if inputs % 2 == 1:
            array.append(inputs)
            sum += inputs
    if len(array) == 0:
        print(-1)
    else:
        print(sum)
        print(min(array))