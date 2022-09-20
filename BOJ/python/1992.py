N = int(input())

graph  = []
for _ in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y, N):
    checkNum = graph[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if checkNum != graph[i][j]:
                print('(', end="")
                for idx in range(2):
                    for idx2 in range(2):
                        dfs(x + idx * (N // 2), y + idx2 * (N // 2), N // 2)
                print(')', end="")
                return
    print(checkNum, end = "")
    

dfs(0, 0, N)