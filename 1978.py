import math

N = int(input())
input_num = list(map(int, input().split()))

count = 0

def isPrime(value):
    for i in range(2, int(math.sqrt(value))+1):
        if value % i == 0:
            return False
    return True

for j in range(N):
    if isPrime(input_num[j]) and input_num[j] != 1:
        count += 1
print(count)