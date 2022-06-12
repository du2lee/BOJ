import sys
from collections import deque

N = int(sys.stdin.readline())

stack = deque(map(int, sys.stdin.readline().split()))
result = deque(-1 for _ in range(N))
count = 0

while stack:
    value = stack.popleft()
    for i in range(len(stack)):
        if value < stack[i]:
            result[count] = stack[i]
            break
    count += 1

print(*result)