M, N = list(map(int, input().split()))

if(M > N):
    print(2 * N - 1)
else:
    print(2 * (M - 1))