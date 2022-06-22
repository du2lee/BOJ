N = int(input())

array = [[1] * 10 for _ in range(N)]

if N > 1:
    for idx in range(1, N):
        for idx2 in range(0, 10):
            array[idx][idx2] = sum(array[idx - 1][:idx2 + 1])
print(sum(array[N - 1]) % 10007)