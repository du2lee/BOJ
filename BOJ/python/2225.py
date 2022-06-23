N, K = list(map(int, input().split()))

row = [1 for _ in range(N)]
dp = [row.copy() for _ in range(K)]

for k in range(1, K):
    for n in range(N):
        if n == 0:
            dp[k][n] = k + 1
        else:
            dp[k][n] = dp[k - 1][n] + dp[k][n - 1]

answer = dp[K - 1][N - 1]
print(answer % 1000000000)