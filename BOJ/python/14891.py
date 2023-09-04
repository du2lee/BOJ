wheels = [0]

for i in range(4):
    arr = []
    for s in input():
        arr.append(int(s))
    wheels.append(arr)


def checkTurn(a, b, direction):
    if wheels[a][2] == wheels[b][6]:
        return 0
    return -direction

def turnWheel(array, direction):
    if direction == 1:
        return [array[-1]] + array[0:-1]
    elif direction == -1:
        return array[1:] + [array[0]]


for _ in range(int(input())):
    check = [0, 0, 0, 0, 0]
    wheel, direction = list(map(int, input().split()))
    check[wheel] = direction

    # 현재 기준에서 오른쪽
    for idx in range(wheel + 1, 5):
        direction = checkTurn(idx - 1, idx, direction)
        check[idx] = direction
        if direction == 0:
            break

    direction = check[wheel]
    # 현재 기준에서 왼쪽
    for idx in range(wheel - 1, 0, -1):
        direction = checkTurn(idx, idx + 1, direction)
        check[idx] = direction
        if direction == 0:
            break

    # check 보면서 톱니바퀴 이동
    for idx in range(1, 5):
        if check[idx] == 0:
            continue
        wheels[idx] = turnWheel(wheels[idx], check[idx])

# 점수체크
score = 0
for idx in range(1, 5):
    score += wheels[idx][0] * (2 ** (idx - 1))
print(score)