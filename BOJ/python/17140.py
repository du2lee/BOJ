def R(graph):
    returnGraph = []
    sortGraph = []
    maxCount = 0
    for row in graph:
        cache = {}
        count = 0
        
        for num in row:
            if num == 0:    # 0일 때 skip
                continue
            if num in cache:
                cache[num] = [cache[num][0] + 1, num]
            else:
                cache[num] = [1, num]
                count += 1
        
        if count > maxCount:
            maxCount = count

        cache = sorted(cache.values())
        sortGraph.append(cache)
    
    maxCount *= 2
        
    # 그래프 다시 그리기
    for row in sortGraph:
        cache = []
        for x, y in row:
            cache.append(y)
            cache.append(x)
        if len(row) < maxCount:
            for _ in range(maxCount - 2 * len(row)):
                cache.append(0)
        returnGraph.append(cache)

    return returnGraph


r, c, k = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(3)]
flag = True

cache = [[0, i + 1] for i in range(100)]

for s in range(101):
    if r - 1 < len(graph) and c - 1 < len(graph[0]): # out of index 처리
        if graph[r - 1][c - 1] == k:
            flag = False
            print(s)
            break

    if len(graph) < len(graph[0]):
        # C연산
        cacheGraph = []
        for row in zip(*graph):
            cacheGraph.append(list(row))
        cacheGraph = R(cacheGraph)
        graph = []
        for row in zip(*cacheGraph):
            graph.append(list(row))
    else:
        # R연산
        graph = R(graph)

if flag:
    print(-1)