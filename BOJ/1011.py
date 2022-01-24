import sys, math

T = int(sys.stdin.readline())
for i in range(T):
    x, y = map(int, sys.stdin.readline().split())

    if y - x == 1 or y - x == 0:
        print(y - x)
    elif math.sqrt(y-x) == int(math.sqrt(y-x)):
        print(int(math.sqrt(y - x)) + int(math.sqrt(y - x)) - 1)
    elif (int(math.sqrt(y - x)) * int(math.sqrt(y - x)) + (int(math.sqrt(y - x)) + 1) * (int(math.sqrt(y - x)) + 1)) / 2 < y - x:
        print(2 * int(math.sqrt(y - x)) + 1)
    else:
        print(2 * int(math.sqrt(y - x)))