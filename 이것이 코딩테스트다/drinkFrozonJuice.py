N, M = list(map(int, input().split()))

graph = [list(map(int, input())) for _ in range(N)]
dx = [1, -1 ,0 ,0]
dy = [0, 0, 1, -1]
count = 0

def dfs(x, y):
    if x < 0 or N - 1 < x or y < 0 or M - 1 < y:
        return

    if graph[x][y] == 0:
        graph[x][y] = 1
        for i in range(4):
            dfs(x + dx[i],y + dy[i])
    return

for x in range(N):
    for y in range(M):
        if graph[x][y] == 0:
            dfs(x, y)
            count += 1
print(count)



# N, M = list(map(int, input().split()))

# graph = []
# count = 0

# for _ in range(N):
#     arr = list(map(int, input()))
#     graph.append(arr)

# def dfs(x, y):
#     if x < 0 or N <= x or y < 0 or M <= y:
#         return False
    
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x , y - 1)
#         dfs(x - 1 , y)
#         dfs(x, y + 1)
#         dfs(x + 1 , y)
#         return True
#     return False

# for i in range(N):
#     for j in range(M): 
#         if dfs(i, j):
#             count += 1

# print(count)


