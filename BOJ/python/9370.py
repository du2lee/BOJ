from heapq import *

T = int(input())
INF = int(10e9)

def func(graph, result ,start):
    q = [(0, start)]
    result[start] = 0

    while q:
        dict, preNode = heappop(q)
        for node, weight in graph[preNode]:
            cost = dict + weight
            if cost < result[node]:
                result[node] = cost
                heappush(q, (cost, node))


for _ in range(T):
    n, m, t = list(map(int, input().split()))
    s, g, h = list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    dest = []   # 도착지
    dictStart = [INF] * (n + 1)
    dictG = [INF] * (n + 1)
    dictH = [INF] * (n + 1)
    answer = []

    for _ in range(m):
        a, b, d = list(map(int, input().split()))
        graph[a].append([b, d])
        graph[b].append([a, d])

    for _ in range(t):
        dest.append(int(input()))

    func(graph, dictStart, s)
    func(graph, dictG, g)
    func(graph, dictH, h)

    for i in dest:
        a = min(dictStart[g] + dictG[h] + dictH[i], dictStart[h] + dictH[g] + dictG[i])
        if dictStart[i] >= a:
            answer.append(i)
    answer.sort()
    print(*answer)
