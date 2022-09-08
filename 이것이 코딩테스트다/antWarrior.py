import sys

N = int(sys.stdin.readline().rstrip())

array = [0] + list(map(int, input().split()))
dp = [0 for _ in range(N + 1)]

dp[1] = array[1]

for i in range(2, N + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + array[i])

print(dp[N])
