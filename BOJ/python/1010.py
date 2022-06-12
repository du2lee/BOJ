import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int,sys.stdin.readline().split())
    mul = 1
    for i in range(1, A+1):
        mul *= (B + 1 - i)
        mul = mul // i
    print(mul)