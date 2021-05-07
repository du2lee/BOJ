import sys

location = sys.stdin.readline()

count = 0

step = [[2, 1], [-2, 1], [-2, -1], [2, -1], [1, 2], [-1, 2], [-1, -2], [1, -2]]


if ord(location[0]) >= 65 and ord(location[0]) <= 90:       # 대문자
    x = ord(location[0]) - 64
elif ord(location[0]) >= 97 and ord(location[0]) <= 122:    # 소문자
    x = ord(location[0]) - 96

y = int(location[1])

if (x >= 1 and x <= 8) and (y >= 1 and y <= 8):  # True input
    pass
else:
    print("값 입력이 올바르지 않습니다.")               # Fasle input
    sys.exit()




for j in step:
    x += j[0]
    y += j[1]
    if (x >= 1 and x <= 8) and (y >= 1 and y <= 8):
        count += 1
    x -= j[0]
    y -= j[1]

print(count)