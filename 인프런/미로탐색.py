N = 7

graph = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N):
    graph.append(list(map(int, input().split())))

answer = 0

def dfs(x, y, graphs):
    global answer

    if x == N - 1 and y == N - 1:
        answer += 1
        return
    
    for idx in range(4):
        nx = dx[idx] + x
        ny = dy[idx] + y
        
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        
        if graphs[nx][ny] != 0:
            continue
        
        graphs[nx][ny] = 1
        dfs(nx, ny, graphs)
        graphs[nx][ny] = 0

graph[0][0] = 1
dfs(0, 0, graph)
print(answer)