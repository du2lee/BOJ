square = []
for _ in range(100):
    square.append([0] * 100)

for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            square[i][j] = 1

result = 0

for x in range(100):
    for y in range(100):
        result += square[x][y]

print(result)

