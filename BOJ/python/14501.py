N = int(input())

works = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for i in range(N + 1)]

for idx in range(N):
    for idx2 in range(idx + works[idx][0], N + 1):
        if dp[idx] + works[idx][1] > dp[idx2]:
            dp[idx2] = dp[idx] + works[idx][1]

print(dp[-1])