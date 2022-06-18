N = int(input())

array = [1] * (N + 1)
array[1] = 1

for idx in range(2, N + 1):
    array[idx] = array[idx - 1] + array[idx - 2]

print(array[N] % 10007)