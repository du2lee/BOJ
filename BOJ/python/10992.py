N = int(input())

for idx in range(N):
    if idx == (N - 1):
        print('*' * (2 * N - 1))
        break
    else:
        print(' ' * (N - idx - 1) + '*' + ' ' * (2 * idx - 1), end="")
    
    if idx != 0:
        print('*', end='')
    print('')