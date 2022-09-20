N = int(input())

graph = []
count = [0, 0 ,0]

for _ in range(N):
    graph.append(list(map(int, input().split())))

def dfs(x, y, N):
    checkNum = graph[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if graph[i][j] != checkNum:
                for idx in range(3):
                    for idx2 in range(3):
                        dfs(x + (N // 3) * idx, y + (N // 3) * idx2, N // 3)
                return
    count[checkNum] += 1

dfs(0, 0, N)

for i in range(-1, 2):
    print(count[i])
    