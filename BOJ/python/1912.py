# import sys
# from collections import deque
# n = int(sys.stdin.readline())
# array = deque(map(int,sys.stdin.readline().split()))


# # result = array[0]                                 #첫번째 방법
# # for i in range(1,len(array)):
# #     if result < array[i]:
# #         result = array[i]
# #     sum = 0
# #     for j in range(i,len(array)):
# #         sum += array[j]
# #         if result < sum:
# #             result = sum
# # print(result)

# dp = [0] * len(array)
# dp[0] = array[0]

# for i in range(1, len(array)):
#     dp[i] = max(dp[i - 1]+ array[i], array[i])

# print(max(dp))



N = int(input())

array = list(map(int, input().split()))

dp = [0] * N
dp[0] = array[0]

for idx in range(1, N):
    dp[idx] = max(array[idx], dp[idx - 1] + array[idx])

print(max(dp))