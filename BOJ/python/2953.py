import sys

max = 0
index = 0
for i in range(1, 6):
    a, b, c, d = map(int, sys.stdin.readline().split())
    if max < a + b + c + d:
        max = a + b + c + d
        index = i
print(index, max)