import sys

T = int(sys.stdin.readline())

array = list(1 for _ in range(101))
array[3], array[4] = 2, 2
for i in range(5, 101):
    array[i] = array[i - 1] + array[i - 5]

for _ in range(T):
    N = int(sys.stdin.readline())
    print(array[N - 1])