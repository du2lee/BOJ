# import sys

# N = int(sys.stdin.readline())

# square = [i * i for i in range(1, 317)]
# value = [0 for _ in range(N + 1)]

# for i in range(1, N + 1):
#     cache = []
#     for j in square:
#         if j > i:
#             break
#         cache.append(value[i - j])
#     value[i] = min(cache) + 1

# print(value[N])


N = int(input())

dp = [0] * (N + 1)
squares = [i * i for i in range(1, 317)]

dp[1] = 1

for idx in range(2, N + 1):
    if idx == 2:
        dp[2] = 2
        continue
    elif idx == 3:
        dp[3] = 3
        continue

    caches = []

    for square in squares:
        if square > idx:
            break
        caches.append(dp[idx - square] + 1)
        
    dp[idx] = min(caches)

print(dp[N])