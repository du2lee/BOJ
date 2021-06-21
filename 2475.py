import sys

a, b, c, d, e = map(int, sys.stdin.readline().split())

value = (a * a + b * b + c * c + d * d + e * e) % 10

print(value)