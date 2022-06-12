import sys

def dfs(graph, start_node):
    visited, need_visit = list(), list()

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited
    
maps = []
N = int(sys.stdin.readline())

graph = dict()
count = 0
save_list = list()

value = list()


for node in range(1, N * N + 1):                                          #key
    graph[node] = []

for _ in range(N):
    col = sys.stdin.readline().split()
    maps.append(col)



for i in range(N):
    for j in range(N):
        count += 1
        if maps[i][0][j] == '1':
            if i == 0:
                if j == 0:
                    if maps[i + 1][0][j] == '1':
                        graph[count].append(count + N)
                    if maps[i][0][j + 1] == '1':
                        graph[count].append(count - 1)
                elif j == str(N - 1):
                    if maps[i + 1][0][j] == '1':
                        graph[count].append(count + N)
                    if maps[i][0][j - 1] == '1':
                        graph[count].append(count - 1)
                else:
                    if maps[i + 1][0][j] == '1':
                        graph[count].append(count + N)
                    if maps[i][0][j - 1] == '1':
                        graph[count].append(count - 1)
                    if maps[i][0][j + 1] == '1':
                        graph[count].append(count + 1)
            elif i == N - 1:
                if j == 0:
                    if maps[i - 1][0][j] == '1':
                        graph[count].append(count - N)
                    if maps[i][0][j + 1] == '1':
                        graph[count].append(count + 1)
                elif j == N - 1:
                    if maps[i - 1][0][j] == '1':
                        graph[count].append(count - N)
                    if maps[i][0][j - 1] == '1':
                        graph[count].append(count - 1)
                else:
                    if maps[i - 1][0][j] == '1':
                        graph[count].append(count - N)
                    if maps[i][0][j - 1] == '1':
                        graph[count].append(count - 1)
                    if maps[i][0][j + 1] == '1':
                        graph[count].append(count + 1)
            else:
                if j == 0:
                    if maps[i - 1][0][j] == '1':
                        graph[count].append(count - N)
                    if maps[i + 1][0][j] == '1':
                        graph[count].append(count + N)
                    if maps[i][0][j + 1] == '1':
                        graph[count].append(count + 1)
                elif j == N - 1:
                    if maps[i - 1][0][j] == '1':
                        graph[count].append(count - N)
                    if maps[i + 1][0][j] == '1':
                        graph[count].append(count + N)
                    if maps[i][0][j - 1] == '1':
                        graph[count].append(count - 1)
                else:
                    if maps[i - 1][0][j] == '1':
                        graph[count].append(count - N)
                    if maps[i + 1][0][j] == '1':
                        graph[count].append(count + N)
                    if maps[i][0][j - 1] == '1':
                        graph[count].append(count - 1)
                    if maps[i][0][j + 1] == '1':
                        graph[count].append(count + 1)

for i in range(1, N * N + 1):
    cache = []
    if len(graph[i]) != 0:
        cache = dfs(graph, i)
        cache.sort()
        if cache not in save_list:
            save_list.append(cache)
            value.append(len(cache))

print(len(value))

value.sort()
for i in value:
    print(i)
print(graph)





'''import sys

dx=[-1,0,1,0]
dy=[0,1,0,-1]
n=int(sys.stdin.readline())
a=[list(sys.stdin.readline()) for _ in range(n)]
cnt=0
apt=[]

def dfs(x,y):
    global cnt
    a[x][y] = '0' #방문한 곳은 0으로
    cnt+=1
    for i in range(4):
        nx = x + dx[i] #i=0일때 (nx,ny)는 좌 , i=1일때 (nx,ny)는 상
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >=n:
            continue
        if a[nx][ny] == '1':
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if a[i][j] == '1':
            cnt= 0
            dfs(i,j)
            apt.append(cnt)

print(len(apt))
apt.sort()
for i in apt:
    print(i)'''