N, M = list(map(int, input().split()))

location = list(map(int,input().split()))
maps = []
check = []

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
result = 1

for _ in range(N):
    row = list(map(int, input().split()))
    check.append([True] * len(row))
    maps.append(row)

check[location[0]][location[1]] = False

while True:
    print(location)
    count = 0
    flag = False
    while count < 4:
        if location[2] == 0:
            location[2] = 3
        else:
            location[2] -= 1
        
        x = location[0] + dx[location[2]]
        y = location[1] + dy[location[2]]

        if (0 > x and x >= N) or (0 > y and y >= M):
            continue

        if maps[x][y] == 0 and check[x][y]:
            location[0] = x
            location[1] = y
            check[x][y] = False
            result += 1
            flag = True
            break
        count += 1
    if flag:
        continue

    x = location[0] - dx[location[2]]
    y = location[1] - dy[location[2]]

    if maps[x][y] == 1:
        break
    else:
        location[0] = x
        location[1] = y

print(result)