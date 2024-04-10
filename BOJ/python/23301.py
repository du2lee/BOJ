N, T = list(map(int, input().split()))

arr = [0] * 1000

for _ in range(N):
    for __ in range(int(input())):
        start, end = list(map(int, input().split()))

        for idx in range(start, end):
            arr[idx] += 1

# 완전탐색
value = -1
answer = 0

for idx in range(1000 - T):
    if value < sum(arr[idx:idx + T]):
        value = sum(arr[idx:idx + T])
        answer = idx

print(answer, end= " ")
print(answer + T)