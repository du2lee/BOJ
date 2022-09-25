from heapq import *

N, E = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
INF = int(10e9)

dictStart = [INF] * (N + 1)
dict1 = [INF] * (N + 1)
dict2 = [INF] * (N + 1)

for i in range(E):
    a, b, c = list(map(int, input().split()))
    graph[a].append([b, c])
    graph[b].append([a, c])

node1, node2 = list(map(int, input().split()))

def func(graph, answer, start):
    queue = [(0, start)]
    answer[start] = 0

    while queue:
        dict, preNode = heappop(queue)
        for node, weight in graph[preNode]:
            cost = dict + weight
            if cost < answer[node]:
                answer[node] = cost
                heappush(queue,(cost, node))

func(graph, dictStart, 1)
func(graph, dict1, node1)
func(graph, dict2, node2)

a = dictStart[node1] + dict1[node2] + dict2[N]
b = dictStart[node2] + dict2[node1] + dict1[N]

if a >= INF or b >= INF:
    print(-1)
else:
    print(min(a, b))