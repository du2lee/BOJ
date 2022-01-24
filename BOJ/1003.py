import sys


def fibonacci(n, count_0, count_1):
    if n == 0:
        print("0")
        count_0 += 1
        return 0
    elif n == 1:
        print("1")
        count_1 += 1
        return 1
    else:
        return fibonacci(n - 1, count_0, count_1) + fibonacci(n - 2, count_0, count_1)


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    count_0 = 0
    count_1 = 0
    fibonacci(N, count_0, count_1)
    print(count_0, count_1)