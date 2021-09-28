import sys
from math import factorial
N, k = map(int, sys.stdin.readline().split())

if 0 <= k and k <= N:
    value = factorial(N) // (factorial(k) * factorial(N - k))
else : 
    value = 0

print(value % 10007)