import math

N = int(input())


def isPrime(Num):
    i = 2
    Num1 = Num
    while True:
        if i > Num1:
            break
        if Num % i == 0:
            print(i)
            Num //= i
        else:
            i += 1

if N == 1:
    pass
else:
    isPrime(N)