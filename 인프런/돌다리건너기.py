dp = [0, 1, 2]

for idx in range(3, int(input()) + 1):
    dp.append(dp[idx - 1] + dp[idx - 2])

print(dp[-1])