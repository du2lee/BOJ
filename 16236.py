import sys

N = int(sys.stdin.readline())
scale = 2
mapp = []
for i in range(N):
    for j in range(N):
        mapp[i] = list(map(int, sys.stdin.readline().split()))