N = int(input())
dp =  [0] * (N + 1)

for i in range(2, N + 1):
    a = b = c = d = i
    if i % 5 == 0:
        a = dp[i // 5] + 1
    if i % 3 == 0:
        b = dp[i // 3] + 1
    if i % 2 == 0:
        c = dp[i // 2] + 1
    d = dp[i - 1] + 1

    dp[i] = min(min(a, b), min(c, d))

print(dp[N])

