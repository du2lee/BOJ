N, M = list(map(int, input().split()))

graph = []
count = 0

for _ in range(N):
    arr = list(map(int, input()))
    graph.append(arr)

def dfs(x, y):
    if x < 0 or N <= x or y < 0 or M <= y:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x , y - 1)
        dfs(x - 1 , y)
        dfs(x, y + 1)
        dfs(x + 1 , y)
        return True
    return False

for i in range(N):
    for j in range(M): 
        if dfs(i, j):
            count += 1

print(count)


