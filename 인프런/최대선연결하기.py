N = int(input())

arr = list(map(int, input().split()))

dp = [1]

answer = 1

for idx in range(1, N):
    cache = 1
    for idx2 in range(idx - 1, -1, -1):
        if arr[idx2] < arr[idx]:
            cache = max(dp[idx2] + 1, cache)

    dp.append(cache)
    answer = max(cache, answer)

print(dp)
print(answer)
