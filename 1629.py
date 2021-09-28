import sys
from math import pow

def func (a, b, c):
    value = int(pow(a , b // 2))
    if b % 2 == 0:
        return value * value % c
    else:
        return value * value * a % c

if __name__ == "__main__":
    a, b, c = map(int, sys.stdin.readline().split())
    print(func(a, b, c))