N, M = list(map(int, input().split()))

maxNum = 0

for _ in range(N):
    arr = list(map(int, input().split()))
    a = min(arr)
    if maxNum < a:
        maxNum = a

print(maxNum)
