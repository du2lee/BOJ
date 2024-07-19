from math import inf

N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

dp = [[inf for _ in range(N)] for _ in range(N)]

dp[0][0] = graph[0][0]

for idx in range(1, N):
    dp[idx][0] = dp[idx - 1][0] + graph[idx][0]
    dp[0][idx] = dp[0][idx - 1] + graph[0][idx]

for x in range(1, N):
    for y in range(1, N):
        dp[x][y] = min(dp[x - 1][y], dp[x][y - 1]) + graph[x][y]

print(dp[N-1][N-1])









# ====== S : Bottom up =======

# N = int(input())

# graph = []

# for _ in range(N):
#     graph.append(list(map(int,  input().split())))

# dp = [[0 for _ in range(N)] for _ in range(N)]

# dp[0][0] = graph[0][0]

# for i in range(1, N):
#     dp[0][i] = dp[0][i - 1] + graph[0][i]
#     dp[i][0] = dp[i - 1][0] + graph[i][0]

# for i in range(1, N):
#     for j in range(1, N):
#         dp[i][j] = graph[i][j] + min(dp[i - 1][j], dp[i][j - 1])

# print(dp[N - 1][N - 1])

# ====== E : Bottom up =======
