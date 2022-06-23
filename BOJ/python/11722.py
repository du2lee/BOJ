N = int(input())

array = list(map(int, input().split()))

dp = [0] * N
dp[0] = 1

for idx in range(N):
    count = 0
    flag = False

    for i in range(len(array[:idx])):
        if array[i] > array[idx] and count < dp[i]:
            count = dp[i]
            flag = True
    
    if flag:
        dp[idx] += count + 1
    else:
        dp[idx] = 1

print(max(dp))