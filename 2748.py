import sys

def func(N):
    if N == 0:
        return 0

    if N == 1:
        return 1

    return func(N - 1) + func(N - 2)


N = int(sys.stdin.readline())

array = list(0 for _ in range(N + 1))

array[1] = 1

for i in range(2, N + 1):
    array[i] = array[i - 1] + array [i - 2]

print(array[N])