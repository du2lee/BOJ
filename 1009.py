import sys

T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    if a % 10 == 0:
        print(10)
        continue
    A = a
    cache = []
    while True:
        cache_2 = a % 10
        if cache_2 in cache:
            break
        cache.append(cache_2)
        a *= A
    if b % len(cache) == 0:
        index = len(cache) - 1
    else:
        index = b % len(cache) - 1
    print(cache[index])