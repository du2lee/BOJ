graph = [input() for _ in range(8)]
count = 0

for i in range(8):
    a = i % 2
    for j in range(0, 7, 2):
        if graph[i][j + a] == 'F':
            count += 1
print(count)