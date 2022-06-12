N = int(input())

for idx in range(1, N + 1):
    print(' ' * (N - idx) + '*' * idx)
for idx in range(N - 1 , 0, -1):
    print(' ' * (N - idx) + '*' * idx)