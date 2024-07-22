N, M = list(map(int, input().split()))

graph = [[0 for _ in range(N + 1)] for __ in range(N + 1)]

for _ in range(M):
    s, e, cost  = list(map(int, input().split()))

    graph[s][e] = cost

for x in range(1, N + 1):
    for y in range(1, N + 1):
        print(graph[x][y], end= " ")
    print()