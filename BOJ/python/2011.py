N = list(map(int, input()))

if N[0] == 0:
    print(0)
else:
    dp = [0] * (len(N) + 1)
    dp[0] = dp[1] = 1
    for idx in range(2, len(N) + 1):
        if N[idx - 1] > 0:
            dp[idx] += dp[idx - 1]
        
        cache = N[idx - 2] * 10 + N[idx - 1]

        if cache <= 26 and 10 <= cache: 
            dp[idx] += dp[idx - 2]

    print(dp[len(N)] % 1000000)