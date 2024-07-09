from copy import deepcopy

N, M = list(map(int, input().split()))

graph = []

for _ in range(N):
    score, time = list(map(int, input().split()))
    graph.append((score, time))

answer = -1

def dfs(n, score, time):
    global answer

    if n >= N:
        answer = max(answer, score)
        return
    
    score1, time1 = graph[n]
    
    # 문제 포함 X
    dfs(n + 1, score, time)
    # 문제 포함
    if time + time1 <= M:
        dfs(n + 1, score + score1, time + time1)
    
dfs(0, 0, 0)
print(answer)