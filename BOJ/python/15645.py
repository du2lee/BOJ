N = int(input())

graph = []

for _ in range(N):
    graph.append(tuple(map(int, input().split())))

F_dp = [graph[0][0]]
S_dp = [graph[0][1]]
T_dp = [graph[0][2]]

f_dp = [graph[0][0]]
s_dp = [graph[0][1]]
t_dp = [graph[0][2]]

for i in range(1, N):
    f_dp.append(min(f_dp[i - 1], s_dp[i - 1]) + graph[i][0])
    s_dp.append(min(min(f_dp[i - 1], s_dp[i - 1]), t_dp[i - 1]) + graph[i][1])
    t_dp.append(min(t_dp[i - 1], s_dp[i - 1]) + graph[i][2])

    F_dp.append(max(F_dp[i - 1], S_dp[i - 1]) + graph[i][0])
    S_dp.append(max(max(F_dp[i - 1], S_dp[i - 1]), T_dp[i - 1]) + graph[i][1])
    T_dp.append(max(T_dp[i - 1], S_dp[i - 1]) + graph[i][2])

print(max(max(T_dp[-1], S_dp[-1]), F_dp[-1]), end= " ")
print(min(min(t_dp[-1], s_dp[-1]), f_dp[-1]))