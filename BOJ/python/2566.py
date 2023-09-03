result = [0, 0, -1]

for i in range(9):
    arr = list(map(int, input().split()))
    for j in range(9):
        if result[2] <= arr[j]:
            result[0] = i + 1
            result[1] = j + 1
            result[2] = arr[j]

print(result[2])
print(result[0], result[1])