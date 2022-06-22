T = int(input())

array = [1] * 11
array[2] = 2
array[3] = 4
for idx in range(4, 11):
    array[idx] = array[idx - 1] + array[idx - 2] + array[idx - 3]

for _ in range(T):
    N = int(input())
    print(array[N])