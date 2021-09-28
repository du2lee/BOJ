import sys

N = int(sys.stdin.readline())

square = [i * i for i in range(1, 317)]
value = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    cache = []
    for j in square:
        if j > i:
            break
        cache.append(value[i - j])
    value[i] = min(cache) + 1

print(value[N])