N, M = list(map(int, input().split()))

graph = [list(map(int, input().split())) for _ in range(N)]

K = int(input())

for _ in range(K):
    count = 0
    a,b,c,d = list(map(int, input().split()))
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    if a == c:
        for y in range(b, d + 1):
            count += graph[a][y]
    else:
        for x in range(a, c + 1):
            for y in range(b, d + 1):
                count += graph[x][y]

    print(count)