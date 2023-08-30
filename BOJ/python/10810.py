N, M = list(map(int, input().split()))

arr = [0] * (N + 1)

for _ in range(M):
    start, end, num = list(map(int, input().split()))
    for i in range(start, end + 1):
        arr[i] = num

for idx in range(1, len(arr)):
    print(arr[idx], end= " ")
print("")