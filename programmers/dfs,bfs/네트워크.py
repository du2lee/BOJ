def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    def dfs(V):
        visited[V] = 1
        
        for i in range(n):
            if i == V:
                continue
            if visited[i] == 0 and computers[V][i] == 1:
                dfs(i)
    
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            answer += 1
        
    return answer