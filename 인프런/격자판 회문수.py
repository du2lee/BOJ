graph = list(list(map(int, input().split())) for _ in range(7))
reverse = list(zip(*graph))

answer = 0

for x in range(7):
    for y in range(3):
        row = graph[x][y : y + 5]

        if row[0] == row[4] and row[1] == row[3]:
            answer += 1

        row = reverse[x][y : y + 5]

        if row[0] == row[4] and row[1] == row[3]:
            answer += 1

print(answer)

        