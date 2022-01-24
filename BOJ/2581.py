import math

M = int(input())
N = int(input())

sum = 0
min = N

def isPrime(value):
    if value == 1:
        return False
    for i in range(2, int(math.sqrt(value))+1):
        if value % i == 0:
            return False
    return True

for j in range(M, N + 1):
    if isPrime(j):
        if min > j:
            min = j
        sum += j

if sum == 0 and min ==N:
    print("-1")
else:
    print(sum)
    print(min)