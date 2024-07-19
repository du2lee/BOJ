N = int(input())

dp = [0, 1, 2]

for idx in range(3, N + 1):
    dp.append(dp[idx - 1] + dp[idx - 2])

print(dp[-1])


# dp = [0, 1, 2]

# N = int(input())

# for idx in range(3, N + 1):
#     dp.append(dp[idx - 1] + dp[idx - 2])
# print(dp[-1])