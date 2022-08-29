N, K = list(map(int, input().split()))

N -= int(K*(K+1)/2)

if N < 0:
    print(-1)
else:
    if N % K == 0:
        print(K - 1)
    else:
        print(K)