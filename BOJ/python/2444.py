N = int(input())
for i in range(1, N):
    cache2 = N - i
    cache = 2 * i - 1
    print(' ' * cache2 + '*' * cache)

for i in range(N, 0, -1):
    cache2 = N - i
    cache = 2 * i - 1
    print(' ' * cache2 + '*' * cache)