N = int(input())

array = list(map(int, input().split()))
dp = [0] * N
dp[0] = 1

for idx in range(1, N):

    maxValue = 0
    index = -1

    for i in range(len(array[:idx])):
        if array[i] < array[idx] and maxValue < dp[i]:
            maxValue = dp[i]
            index = i


    if index != -1:
        dp[idx] += dp[index] + 1
    else:
        dp[idx] = 1

print(max(dp))