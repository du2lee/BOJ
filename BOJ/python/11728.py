N, M = list(map(int, input().split()))

arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

answer = arr + arr2
answer.sort()

print(*answer)

