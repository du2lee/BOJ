N = int(input())

array = list(map(int, input().split()))
array = [0] + array
dp = [0] * (N + 1)
dp[1] = array[1]

for idx in range(2, N + 1):
    cache = []
    for i in range(idx):
        cache.append(dp[i] + array[idx - i])
    dp[idx] = max(cache)

print(dp[-1])