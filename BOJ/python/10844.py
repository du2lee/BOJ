N = int(input())

array = [[0] * 10 for _ in range(N)]
array[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

if N > 1:
    for idx in range(1, N):
        for idx2 in range(10):
            if idx2 == 0:
                array[idx][0] = array[idx - 1][1]
            elif idx2 == 9:
                array[idx][9] = array[idx - 1][8]
            else:
                array[idx][idx2] = array[idx - 1][idx2 - 1] + array[idx - 1][idx2 + 1]
answer = sum(array[N - 1]) % 1000000000
print(answer)