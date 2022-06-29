import math

a, b = list(map(int, input().split()))
result = math.gcd(a, b)
print('1' * result)

