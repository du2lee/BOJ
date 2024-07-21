from math import inf

N, M = list(map(int, input().split()))

dp = [[inf for _ in range(N + 1)] for __ in range(N + 1)]

for idx in range(N + 1):
    dp[idx][idx] = 0

for _ in range(M):
    s, e, cost = list(map(int, input().split()))
    dp[s][e] = cost

for idx in range(1, N + 1):
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            dp[x][y] = min(dp[x][y], dp[x][idx] + dp[idx][y])

for x in range(1, N + 1):
    for y in range(1, N + 1):
        if dp[x][y] != inf:
            print(dp[x][y], end = " ")
        else:
            print("M", end = " ")
    print()


# from math import inf

# N, M = list(map(int, input().split()))

# graph = [[inf for _ in range(N + 1)] for __ in range(N + 1)]

# for i in range(N):
#     graph[i + 1][i + 1] = 0 

# for _ in range(M):
#     s, e, cost = list(map(int, input().split()))
#     graph[s][e] = cost

# for idx in range(1, N + 1):
#     for i in range(1, N + 1):
#         for j in range(1, N + 1):
#             graph[i][j] = min(graph[i][j], graph[i][idx] + graph[idx][j])

# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         if graph[i][j] == inf:
#             print("M", end= " ")
#         else:
#             print(graph[i][j], end= " ")
#     print()