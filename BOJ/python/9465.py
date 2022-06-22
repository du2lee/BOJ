T = int(input())

for _ in range(T):
    array = [0, 0]

    N = int(input())
    array[0] = list(map(int, input().split()))
    array[1] = list(map(int, input().split()))
    for idx in range(1, N):
        if idx == 1:
            array[1][idx] += array[0][0]
            array[0][idx] += array[1][0]
        else:
            array[1][idx] += max(array[0][idx - 1], array[0][idx - 2])
            array[0][idx] += max(array[1][idx - 1], array[1][idx - 2])
    
    print(max(array[0][N - 1], array[1][N - 1]))