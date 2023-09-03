i, j  = list(map(int, input().split()))
arr = [0]

def function(start, end, arr):
    array = []
    for idx in range(end, start - 1, -1):
        array.append(arr[idx])
    return array

for idx in range(i):
    arr.append(idx + 1)

for _ in range(j):
    start, end = list(map(int, input().split()))
    arr[start:end + 1] = function(start, end, arr)

for idx in range(1, len(arr)):
    print(arr[idx], end= " ")
print("")
