N = int(input())

graph = []
count_1 = 0
count_0 = 0

for i in range(N):
    graph.append(list(map(int, input().split())))

def division(x, y, N):
    global count_0, count_1
    check = graph[x][y]
    for dx in range(x, x + N):
        for dy in range(y, y + N):
            if graph[dx][dy] != check:
                cache = N // 2
                for i in range(2):
                    for j in range(2):
                        division(x + (i * cache),y + (j * cache), cache)
                return
    if check == 1:
        count_1 += 1
    elif check == 0:
        count_0 += 1

division(0, 0, N)

print(count_0)
print(count_1)
