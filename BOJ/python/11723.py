import sys

N = int(sys.stdin.readline().rstrip())
arr = set()

for _ in range(N):
    cache = sys.stdin.readline().rstrip().split()

    if len(cache) == 1:
        if cache[0] == 'all':
            arr = set([i for i in range(1, 21)])
        elif cache[0] == 'empty':
            arr = set()
    else:
        cache[1] = int(cache[1])
        if cache[0] == 'add':
            arr.add(cache[1])
        elif cache[0] == 'remove':
            arr.discard(cache[1])
        elif cache[0] == 'check':
            if cache[1] in arr:
                print(1)
            else:
                print(0)
        elif cache[0] == 'toggle':
            if cache[1] in arr:
                arr.discard(cache[1])
            else:
                arr.add(cache[1])