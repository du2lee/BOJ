import sys
N, X = map(int, sys.stdin.readline().split())
list_N = list(map(int, sys.stdin.readline().split()))
for i in list_N:
    if i < X:
        print(i, end=' ')
print("")