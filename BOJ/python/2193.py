N = int(input())

array = [[0]* 2 for _ in range(N)]

array[0] = [0, 1]

for idx in range(1, N):
    for idx2 in range(2):
        if idx2 == 0:
            array[idx][idx2] = array[idx - 1][0] + array[idx - 1][1]
        else:
            array[idx][idx2] = array[idx - 1][0]

print(sum(array[N - 1]))