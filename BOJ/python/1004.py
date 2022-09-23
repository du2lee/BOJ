import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    x1, y1, x2, y2 = list(map(int, sys.stdin.readline().rstrip().split()))
    N = int(sys.stdin.readline().rstrip())
    count = 0
    for _ in range(N):
        cx, cy, r = list(map(int, sys.stdin.readline().rstrip().split()))
        a = (cx - x1) ** 2 + (cy - y1) ** 2
        b = (cx - x2) ** 2 + (cy - y2) ** 2
        c = r ** 2
        if (a <= c and b <= c) or (a >= c and b >= c):
            pass
        else:
            count += 1
    print(count)