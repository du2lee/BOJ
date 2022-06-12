import sys

def func(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    return func (N - 1) + func(N - 2)


N = int(sys.stdin.readline())

print(func(N))