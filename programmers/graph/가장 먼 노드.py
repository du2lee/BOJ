from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
    
    def bfs(start):
        q = deque([(start,1)])
        visited[start] = 1
        while q:
            v, l = q.popleft()
            for i in graph[v]:
                if visited[i] == 0:
                    visited[i] = l + 1
                    q.append((i, l + 1))
            
    bfs(1)
    maxValue = 0
    for i in range(n):
        if maxValue < visited[i + 1]:
            maxValue = visited[i + 1]
            answer = 1
        elif maxValue == visited[i + 1]:
            answer += 1
    
    return answer