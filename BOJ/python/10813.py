N, M = list(map(int, input().split()))

arr = []

for i in range(N):
    arr.append(i + 1)

for _ in range(M):
    a, b = list(map(int, input().split()))
    cache = arr[a - 1]
    arr[a - 1] = arr[b - 1]
    arr[b - 1] = cache

for i in range(N):
    print(arr[i], end= " ")
print("")