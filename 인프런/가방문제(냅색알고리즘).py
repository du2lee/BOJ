N, maxKgs = list(map(int, input().split()))

pocket = []

for _ in range(N):
    pocket.append(list(map(int, input().split())))

dp = [0 for _ in range(maxKgs + 1)]

for w, v in pocket:
    for idx in range(w, maxKgs + 1):
        dp[idx] = max(v + dp[idx - w], dp[idx])

print(dp[-1])