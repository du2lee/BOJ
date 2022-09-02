N, M, K = list(map(int, input().split()))
array = list(map(int, input().split()))
array.sort(reverse=True)
# 위는 공통

first = array[0]
dp = array[0] * (K - 1) + array[1]

summary = dp * (M // K) + first * (M % K)

print(summary)




# # M이 100억 이상이면 시간초과 남
# summary = 0
# count = 0 
# first = array[0]
# second = array[1]

# for idx in range(M):
#     if count >= K:
#         summary += second
#         count = 0
#     else:
#         summary += first
#         count += 1

# print(summary)
