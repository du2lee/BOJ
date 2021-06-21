import sys

N = int(sys.stdin.readline())
array = list(i for i in map(int, sys.stdin.readline().split()))
M = max(array)
m = min(array)
print(M * m)