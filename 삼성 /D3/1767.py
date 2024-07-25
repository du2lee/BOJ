from math import inf
from copy import deepcopy

for i in range(int(input())):
    N = int(input())

    graph = []
    p = []

    for x in range(N):
        row = list(map(int, input().split()))
        for y in range(N):
            if row[y] == 1:
                p.append((x, y))
        graph.append(row)
    
    answer = inf
    countCore = 0

    def dfs(n, value, graph, core):
        global answer
        global countCore

        if countCore > core:
            return

        if n >= len(p):
            if countCore < core:
                countCore = core
                answer = value
            elif countCore == core:
                answer = min(answer, value)
            return
        
        x, y = p[n]

        if x <= 0 or y <= 0 or x >= N - 1 or y >= N - 1:
            dfs(n + 1, value, graph, core)
            return
        
        cacheGraph = deepcopy(graph)
        
        flag = True
        cache = 0

        for idx in range(x):
            if graph[idx][y] == 1:
                flag = False
                break
            graph[idx][y] = 1
            cache += 1

        if flag:
            dfs(n + 1, value + cache, graph, core)

        graph = deepcopy(cacheGraph)

        flag = True
        cache = 0

        for idx in range(N - 1, x, -1):
            if graph[idx][y] == 1:
                flag = False
                break
            graph[idx][y] = 1
            cache += 1

        if flag:
            dfs(n + 1, value + cache, graph, core)

        graph = deepcopy(cacheGraph)

        flag = True
        cache = 0

        for idx in range(y):
            if graph[x][idx] == 1:
                flag = False
                break
            graph[x][idx] = 1
            cache += 1

        if flag:
            dfs(n + 1, value + cache, graph, core)

        graph = deepcopy(cacheGraph)

        flag = True
        cache = 0

        for idx in range(N - 1, y, -1):
            if graph[x][idx] == 1:
                flag = False
                break
            graph[x][idx] = 1
            cache += 1

        if flag:
            dfs(n + 1, value + cache, graph, core)

        graph = deepcopy(cacheGraph)

        dfs(n + 1, value, graph, core - 1)

    dfs(0, 0, graph, len(p))
    print("#" + str(i + 1) + " " + str(answer))