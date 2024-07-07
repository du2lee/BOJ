N = int(input())
coins = list(map(int, input().split()))
money = int(input())

coins.sort()

dp = [1000 for _ in range(money + 1)]

for idx in range(coins[0]):
    dp[idx] = 0

for coin in coins:
    for idx in range(coin, money + 1):
        dp[idx] = min(dp[idx], 1 + dp[idx - coin])

print(dp[-1])