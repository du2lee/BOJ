import sys
from math import factorial

N, k = map(int, sys.stdin.readline().split())

value = factorial(N) // (factorial(k) * factorial(N - k))

print(value)