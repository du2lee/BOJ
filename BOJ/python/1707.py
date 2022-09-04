from collections import deque
K = int(input())

graph = []
visited = [] 

def bfs(start, color):
    queue = deque([start])
    visited[start] = color

    while queue:
        value = queue.popleft()
        color = visited[value]
        for i in graph[value]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = -color
            elif visited[i] == color:
                return False
    return True
            
for _ in range(K):
    V, E = list(map(int, input().split()))
    
    graph = [[] for _ in range(V + 1)]
    visited = [0 for _ in range(V + 1)]
    flag = True

    for _ in range(E):
        a, b = list(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)

    for idx in range(1, V + 1):
        if visited[idx] == 0:
            flag = bfs(idx, 1)
        if not flag:
            break

    if flag:
        print('YES')
    else:
        print('NO')
