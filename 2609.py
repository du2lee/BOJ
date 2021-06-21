import sys

A, B = map(int, sys.stdin.readline().split())

def func(a, b):
    mins = min(a,b)
    gcd = 1
    lcm = a * b
    value_a = a
    value_b = b
    for i in range(2,mins + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
            value_a = a // i
            value_b = b // i

    if gcd == 1:
        print(gcd)
        print(lcm)
    else : 
        print(gcd)
        lcm = gcd * value_a * value_b
        print(lcm)

func(A, B)