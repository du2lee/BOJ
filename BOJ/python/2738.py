N, M = map(int, input().split())

matrix1 = []
matrix2 = []

for _ in range(N):
    arr = list(map(int, input().split()))
    matrix1.append(arr)

for _ in range(N):
    arr = list(map(int, input().split()))
    matrix2.append(arr)

for i in range(N):
    for j in range(M):
        print(matrix1[i][j] + matrix2[i][j] ,end = " ")
    print("")