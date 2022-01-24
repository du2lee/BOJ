import sys
while True:
    A, B = map(int, sys.stdin.readline().split())
    if (0 < A and B < 10):
        print(A + B)
    else:
        break
