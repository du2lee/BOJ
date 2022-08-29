N = int(input())

apples = 0

for i in range(N):
    a, b = list(map(int, input().split()))
    apples += b % a

print(apples)