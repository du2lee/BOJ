N = int(input())

array = [0] * N

for idx in range(N):
    array[idx] = int(input())

array.sort()

for idx in array:
    print(idx)