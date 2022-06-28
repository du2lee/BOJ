N = int(input())

array = [0] * N

for idx in range(N):
    array[idx] = list(map(str, input().split()))
    for i in range(1, 4):
        array[idx][i] = int(array[idx][i])

array.sort(key= lambda x:(-x[1], x[2], -x[3], x[0]))

for idx in array:
    print(idx[0])