N = int(input())

for idx in range(N, 1, -1):
    print(' ' * (N-idx) + '*' * (2 * idx - 1))

for idx in range(1, N + 1):
    print(' ' * (N-idx) + '*' * (2 * idx - 1))