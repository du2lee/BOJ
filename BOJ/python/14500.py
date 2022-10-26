N, M = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(N)]

answer = 0

for i in range(N):         # 가로 4개
    for j in range(M - 3):
        answer = max(answer, sum(graph[i][j:j+4]))

for i in range(N - 3):      # 세로 4개
    for j in range(M):
        cache = 0
        for k in range(4):         
            cache += graph[i + k][j]
        answer = max(answer, cache)

for i in range(N - 1):      # 2 X 3
    for j in range(M - 2):
        result = 0
        result = max(result, graph[i][j] + graph[i][j + 1] + graph[i][j + 2] + graph[i + 1][j])
        result = max(result, graph[i][j] + graph[i][j + 1] + graph[i][j + 2] + graph[i + 1][j + 1])
        result = max(result, graph[i][j] + graph[i][j + 1] + graph[i][j + 2] + graph[i + 1][j + 2])
        result = max(result, graph[i + 1][j] + graph[i + 1][j + 1] + graph[i + 1][j + 2] + graph[i][j])
        result = max(result, graph[i + 1][j] + graph[i + 1][j + 1] + graph[i + 1][j + 2] + graph[i][j + 1])
        result = max(result, graph[i + 1][j] + graph[i + 1][j + 1] + graph[i + 1][j + 2] + graph[i][j + 2])
        result = max(result, graph[i + 1][j] + graph[i + 1][j + 1] + graph[i][j + 2] + graph[i][j + 1])
        result = max(result, graph[i][j] + graph[i][j + 1] + graph[i + 1][j + 2] + graph[i + 1][j + 1])
        answer = max(answer, result)

for i in range(N - 2):      # 3 X 2
    for j in range(M - 1):

        result = 0
        result = max(result, graph[i][j] + graph[i + 1][j] + graph[i + 2][j] + graph[i][j + 1])
        result = max(result, graph[i][j] + graph[i + 1][j] + graph[i + 2][j] + graph[i + 1][j + 1])
        result = max(result, graph[i][j] + graph[i + 1][j] + graph[i + 2][j] + graph[i + 2][j + 1])
        result = max(result, graph[i][j + 1] + graph[i + 1][j + 1] + graph[i + 2][j + 1] + graph[i][j])
        result = max(result, graph[i][j + 1] + graph[i + 1][j + 1] + graph[i + 2][j + 1] + graph[i + 1][j])
        result = max(result, graph[i][j + 1] + graph[i + 1][j + 1] + graph[i + 2][j + 1] + graph[i + 2][j])
        result = max(result, graph[i][j] + graph[i + 1][j] + graph[i + 1][j + 1] + graph[i + 2][j + 1])
        result = max(result, graph[i + 2][j] + graph[i + 1][j] + graph[i + 1][j + 1] + graph[i][j + 1])

        answer = max(answer, result)

for i in range(N - 1):      # 2 X 2
    for j in range(M - 1):
        answer = max(answer, graph[i][j] + graph[i][j + 1] + graph[i + 1][j] + graph[i + 1][j + 1])

print(answer)