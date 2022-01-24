import sys

T = int(sys.stdin.readline())

#def func(k, N):                # 재귀함수로 풀이
#    if k == 0:
#        return N
#    if N == 1:
#        return 1
#    return (func(k - 1, N) + func(k , N - 1))


for i in range(T):
    k = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    print(func(k,N))