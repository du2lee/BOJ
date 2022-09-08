import sys

N, M = list(map(int, sys.stdin.readline().rstrip().split()))

moneys = []
dp = [0] + [10001] * M 

for _ in range(N):
    moneys.append(int(sys.stdin.readline().rstrip()))

moneys.sort()


for i in moneys:
    for j in range(i, M + 1):
        if dp[j - i] != 10001: 
            dp[j] = min(dp[j], dp[j - i] + 1)
if dp[M] == 10001:
    print(-1)
else:            
    print(dp[M])
