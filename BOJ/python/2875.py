import sys

N, M, K = map(int,sys.stdin.readline().split())

modPeople = 0

if N > (2 * M):
    modPeople = N - (2 * M)
elif N < (2 * M):
    modPeople = ((2 * M) - N) // 2 + ((2 * M) % 2)

K -= modPeople

if K > 0:

    value = M + N - modPeople - K
    value //= 3

    if value < 0:
        print(0)
    else:
        print(value)
else:
    print((N + M - modPeople)// 3)