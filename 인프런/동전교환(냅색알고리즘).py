N = int(input())
coins = list(map(int, input().split()))
M = int(input())

coins.sort()

dp = [0 for _ in range(M + 1)]

for coin in coins:
    for idx in range(coin, M + 1):
        if dp[idx] == 0:
            dp[idx] = dp[idx - coin] + 1
        else:
            dp[idx] = min(dp[idx - coin] + 1, dp[idx])

print(dp[-1])



# N = int(input())
# coins = list(map(int, input().split()))
# money = int(input())

# coins.sort()

# dp = [1000 for _ in range(money + 1)]

# for idx in range(coins[0]):
#     dp[idx] = 0

# for coin in coins:
#     for idx in range(coin, money + 1):
#         dp[idx] = min(dp[idx], 1 + dp[idx - coin])

# print(dp[-1])