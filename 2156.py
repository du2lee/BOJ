import sys

n = int(sys.stdin.readline())
array = []

for i in range(n):
    cache = int(sys.stdin.readline())
    array.append(cache)

dp = [0] * n

if n >= 4:
    dp[0] = array[0]
    dp[1] = array[0] + array[1]
    dp[2] = max(dp[1], array[0] + array[2], array[1] + array[2])
    for i in range(3, n):
        dp[i] = max(dp[i - 1], array[i] + dp[i - 2], array[i] + array[i - 1]+ dp[i - 3])
    print(max(dp))
elif n == 1 or n == 2:
    print(sum(array))
else:
    a = array[0] + array[1]
    b = array[1] + array[2]
    print(max(a,b))