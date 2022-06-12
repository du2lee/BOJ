import sys, math


def isPrime(N):
    count = 0
    for i in range(N + 1, 2 * N + 1):
        a =False
        if i == 1:
            pass
        else:
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    a = True
                    break
            if a == False:
                count += 1
    return count

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    print(isPrime(n))
