import sys

while True:

    A, B = map(int, sys.stdin.readline().split())

    if A == 0 and B == 0:
        break

    if A > B:
        if int(A / B) == A / B:
            print("multiple")
        else:
            print("neither")
    
    elif A < B:
        if int(B / A) == B / A:
            print("factor")
        else:
            print("neither")