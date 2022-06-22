# import sys

# n = int(sys.stdin.readline())
# array = []

# for i in range(n):
#     cache = int(sys.stdin.readline())
#     array.append(cache)

# dp = [0] * n

# if n >= 4:
#     dp[0] = array[0]
#     dp[1] = array[0] + array[1]
#     dp[2] = max(dp[1], array[0] + array[2], array[1] + array[2])
#     for i in range(3, n):
#         dp[i] = max(dp[i - 1], array[i] + dp[i - 2], array[i] + array[i - 1]+ dp[i - 3])
#     print(max(dp))
# elif n == 1 or n == 2:
#     print(sum(array))
# else:
#     a = array[0] + array[1]
#     b = array[1] + array[2]
#     print(max(a,b))




N = int(input())
array = [0] * N
dp = [0] * N
for idx in range(N):
    array[idx] = int(input())

if N == 1 or N == 2:
    print(sum(array[0:N + 1]))
else:
    dp[0] = array[0]
    dp[1] = sum(array[0:2])
    
    for idx2 in range(2, N):
        dp[idx2] = max(dp[idx2 - 1], dp[idx2 - 2] + array[idx2], dp[idx2 - 3] + array[idx2] + array[idx2 - 1])
    print(dp[N - 1])