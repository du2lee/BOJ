N = int(input())

graph = []

for _ in range(N):
    graph.append(tuple(map(int, input().split())))

F_dp = graph[0][0]
S_dp = graph[0][1]
T_dp = graph[0][2]

f_dp = graph[0][0]
s_dp = graph[0][1]
t_dp = graph[0][2]

for i in range(1, N):
    a = F_dp
    b = S_dp
    c = T_dp

    d = f_dp
    e = s_dp
    f = t_dp

    f_dp = min(d, e) + graph[i][0]
    s_dp = min(min(d, e), f) + graph[i][1]
    t_dp = min(f, e) + graph[i][2]

    F_dp = max(a, b) + graph[i][0]
    S_dp = max(max(a, b), c) + graph[i][1]
    T_dp = max(c, b) + graph[i][2]

print(max(max(T_dp, S_dp), F_dp), end= " ")
print(min(min(t_dp, s_dp), f_dp))