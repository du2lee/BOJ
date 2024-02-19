sdoku = [list(map(int, input().split())) for _ in range(9)]

flag = False

for row in sdoku:
    if flag:
        break
    check = [False for _ in range(10)]
    for value in row:
        if check[value]:
            flag = True
            break
        check[value] = True

for column in zip(*sdoku):
    if flag:
        break
    check = [False for _ in range(10)]
    for value in row:
        if check[value]:
            flag = True
            break
        check[value] = True

for x in range(0, 7, 3):
    if flag:
        break
    for y in range(0, 7, 3):
        if flag:
            break
        check = [False for _ in range(10)]
        for nx in range(x, x + 3):
            if flag:
                break
            for ny in range(y, y + 3):
                value = sdoku[nx][ny]
                if check[value]:
                    flag = True
                    break
                check[value] = True

if flag:
    print('NO')
else:
    print('YES')
        

