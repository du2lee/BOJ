N, M = list(map(int, input().split()))

graph = [[0 for _ in range(N + 1)] for __ in range(N + 1)]

for _ in range(M):
    s, e = list(map(int, input().split()))
    graph[s][e] = 1

answer = 0
check = [False for _ in range(N + 1)]

def dfs(s, graph):
    global answer
    if s == N:
        answer += 1
        return
    
    for idx in range(1, N + 1):
        if graph[s][idx] == 1:
            if check[idx]:
                continue
            check[idx] = True
            graph[s][idx] = 0
            dfs(idx, graph)
            graph[s][idx] = 1
            check[idx] = False

check[1] = True
dfs(1, graph)
print(answer)
