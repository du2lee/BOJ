array = []
for _ in range(16):
    array.append([1] * 14)

for i in range(1, 16):
    for j in range(14):
        count = 0
        for k in range(j + 1):
            count += array[i - 1][k]
        array[i][j] = count
array = array[1:]


T = int(input())

for _ in range(T):
    a = int(input())
    b = int(input())
    print(array[a][b - 1])