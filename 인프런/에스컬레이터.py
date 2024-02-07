import math

N = int(input())

dp = [[math.inf, math.inf, math.inf] for _ in range(N)]
maps = []

location = 1

for _ in range(N):
    row = list(input())
    maps.append(row)

# 1층 초기화
for idx in range(3):
    if maps[0][idx] == '0':
        if idx == 1:
            dp[0][idx] = 0
        else:
            dp[0][idx] = 1

for h in range(1, N):
    for idx in range(3):
        if maps[h][idx] == '0':
            cache = math.inf
            for idx2 in range(3):
                if idx == idx2:
                    cache = min(cache, dp[h - 1][idx2])
                else:
                    cache = min(cache, dp[h - 1][idx2] + abs(idx2 - idx))

            dp[h][idx] = cache

print(min(dp[-1]))

    
