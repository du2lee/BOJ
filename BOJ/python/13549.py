from collections import deque

N, M= list(map(int, input().split()))

graph = [-1] * 100001

graph[N] = 0

q = deque([N])

while q:
    v = q.popleft()
    if v == M:
        break

    a = v * 2
    b = v - 1
    c = v + 1
    if a >= 0 and a < 100001 and graph[a] == -1:
        graph[a] = graph[v]
        q.append(a)

    if b >= 0 and b < 100001 and graph[b] == -1:
        graph[b] = graph[v] + 1
        q.append(b)
    
    if c >= 0 and c < 100001 and graph[c] == -1:
        graph[c] = graph[v] + 1
        q.append(c)
    
print(graph[M])
