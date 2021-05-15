import sys, math

M, N = map(int, sys.stdin.readline().split())

def isPrime(M, N):
    for i in range(M, N + 1):
        if i == 1:
            pass
        else:
            a = False
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    a = True
                    break
            if a == False:
                print(i)

isPrime(M, N)