import sys

def factorial(N):
    if N == 1 or N == 0:
        return 1
    return N * factorial(N - 1)

N = int(sys.stdin.readline())

print(factorial(N))