import sys

N = int(sys.stdin.readline())

answer = 0

for i in range(1, N + 1):
    value = list(map(int,str(i)))
    if N == i + sum(value):
        print(i)
        break
    
    if N == i:
        print(0)