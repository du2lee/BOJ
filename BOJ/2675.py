import sys

N = int(sys.stdin.readline())
for i in range(N):
    R, S = map(str, sys.stdin.readline().split()) 
    for j in range(len(S)):
        for k in range(int(R)):
            print(S[j], end="")
    print("")