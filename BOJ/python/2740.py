N, M = list(map(int, input().split()))

A = []
for i in range(N):
    A.append(list(map(int, input().split())))

M, K = list(map(int, input().split()))

B = []
for i in range(M):
    B.append(list(map(int, input().split())))

answer = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            answer[i][j] += A[i][k] * B[k][j]

for i in answer:
    print(*i)
