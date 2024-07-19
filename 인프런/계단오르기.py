N = int(input())

dp = [0, 1, 2]

for idx in range(3, N + 1):
    dp.append(dp[idx - 1] + dp[idx - 2])

print(dp[-1])


# def func(N):
#     if N == 1:
#         return 1
#     elif N == 2:
#         return 2
    
#     return func(N - 1) + func(N - 2)

# print(func(int(input())))