N, F = list(map(int, input().split()))

N1 = N - 1

combi = [1]

for idx in range(1, N1):
    cache = 1
    for i in range(N1, N1 - idx, -1):
        cache *= i
    for i in range(1, idx + 1):
        cache //= i

    combi.append(cache)

combi.append(1)

check = [False for _ in range(N + 1)]

def func(arr):
    cache = 0

    if len(arr) == 1:
        return arr[0]
    
    for idx in range(len(arr)):
        cache += combi[idx] * arr[idx]

    return cache

def dfs(n, arr, check):
    if n > N:
        if F == func(arr):
            for v in arr:
                print(v, end=" ")
            print()
            exit()
        return
    
    for idx in range(1, N + 1):
        if check[idx]:
            continue
        check[idx] = True
        dfs(n + 1, arr + [idx], check)
        check[idx] = False

dfs(1, [], check)