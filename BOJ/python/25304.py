X = int(input())
N = int(input())

sum = 0

for _ in range(N):
    arr = list(map(int, input().split()))
    sum += arr[0] * arr[1]

if sum == X:
    print('Yes')
else:
    print('No')