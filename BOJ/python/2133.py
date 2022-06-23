N = int(input())

if N % 2 == 1:
    print(0)
else:
    dp = [0] * (N + 1)
    dp[2] = 3

    for idx in range(4, N + 1, 2):
        
        for idx2 in range(idx - 4 , 1, -2):
            dp[idx] += dp[idx2] * 2
        
        dp[idx] += dp[idx - 2] * dp[2]
        dp[idx] += 2

    print(dp[N])