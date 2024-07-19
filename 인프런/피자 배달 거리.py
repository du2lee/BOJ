from math import inf

N, M = list(map(int, input().split()))

graph = []

pizza = []
house = []
answer = inf


for x in range(N):
    row = list(map(int, input().split()))

    for y in range(N):
        if row[y] == 1:
            house.append((x, y))
        elif row[y] == 2:
            pizza.append((x, y))

    graph.append(row)

answer = inf

def dfs(idx, n, pickPizza):
    global answer

    if idx >= len(pizza):
        return

    if n == M:
        cache2 = 0
        for x, y in house:
            cache = inf
            for px, py in pickPizza:
                cache = min(cache, abs(x - px) + abs(y - py))

            cache2 += cache

        answer = min(answer, cache2)
        return
    
    dfs(idx + 1, n + 1, pickPizza + [pizza[idx]])

    dfs(idx + 1, n, pickPizza)
    
dfs(0, 0, [])

print(answer)