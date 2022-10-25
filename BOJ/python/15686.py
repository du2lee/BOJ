from itertools import combinations

N, M = list(map(int, input().split()))

graph = [list(map(int, input().split())) for _ in range(N)]

chicken = [] # 치킨집 목록
houses = []  # 집 목록

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            houses.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

answer = 100000

for cache in list(combinations(chicken, M)):
    result = 0
    for x, y in houses:
        mValue = 100000
        for nx, ny in cache:
            a = abs(x - nx) + abs(y - ny)
            if mValue > a:
                mValue = a
        result += mValue
        if result >= answer:
            continue    
    answer = min(answer, result)

print(answer)