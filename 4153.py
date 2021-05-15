import sys

while True:

    a, b, c = map(int, sys.stdin.readline().split())

    if a == 0 or b == 0 or c == 0:
        break

    if a * a == b * b + c * c or b * b == a * a + c * c or c * c == b * b + a * a:
        print("right")
    else:
        print("wrong")