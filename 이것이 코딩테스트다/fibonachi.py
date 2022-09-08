# 재귀로 표현(단순 계산)
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

# loop로 표현(dp)
dp = [1, 1]

for i in range(N):
    value = dp[i - 1] + dp[i - 2]
    dp.append(value)
print(dp[N - 1])


a = int(input())
print(fibo(a))