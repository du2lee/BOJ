import sys, math

T = int(sys.stdin.readline())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    r = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))




    if x1 == x2 and y1==y2 and r1 == r2:
        print("-1")
    elif r  > r2 + r1 or r < abs(r2 - r1):
        print("0")
    elif r == r2 + r1 or r == abs(r2 - r1):     
        print("1")
    else:
        print("2")
