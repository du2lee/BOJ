N = int(input())

array = list(map(int, input().split()))

dp = [0] * N
dp[0] = array[0]

for idx in range(N):
    maxValue = 0
    index = -1

    for i in range(len(array[:idx])):
        if array[i] < array[idx] and maxValue < dp[i]:
            maxValue = dp[i]
            index = i

    if index != -1:
        dp[idx] = maxValue + array[idx]
    else:
        dp[idx] = array[idx]

print(max(dp))