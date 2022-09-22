import sys

N, M = list(map(int, sys.stdin.readline().rstrip().split()))

getWords = dict()
count = 0
for _ in range(N):
    getWords[sys.stdin.readline().rstrip()] = True

for _ in range(M):
    try:
        if getWords[sys.stdin.readline().rstrip()]:
            count += 1
    except:
        pass
    
print(count)