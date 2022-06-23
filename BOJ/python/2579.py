N = int(input())
array = [0] * N

for idx in range(N):
    array[idx] = int(input())

dp = [0] * N
dp[0] = array[0]

for idx in range(1, N):
    if idx == 1:
        dp[idx] = array[idx] + dp[idx - 1]
    elif idx == 2:
        dp[idx] = max(array[0] + array[2], array[1]+ array[2])
    else:
        dp[idx] = max(dp[idx - 2] + array[idx], dp[idx - 3] + array[idx] + array[idx - 1])
   
print(dp[N - 1])