N = int(input())
num = int(input())
sum = 0
for i in range(N):
    cache = num % 10
    num = num // 10
    sum += cache

print(sum)