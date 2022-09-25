from heapq import *

V, E = list(map(int, input().split()))
K = int(input())
graph = [[] for _ in range(V + 1)]
INF = 100000000
result = [INF] * (V + 1)


for i in range(E):
    cache = list(map(int, input().split()))
    graph[cache[0]].append(cache[1:])


def dfs(start):
    queue = [(0, start)]
    result[start] = 0
    
    while queue:
        dict, now = heappop(queue)

        for node, weight in graph[now]:
            cost = dict + weight
            if result[node] > cost:
                result[node] = cost
                heappush(queue, (cost, node))

dfs(K)

for i in range(1, V + 1):
    if INF == result[i]:
        print('INF')
    else:
        print(result[i])