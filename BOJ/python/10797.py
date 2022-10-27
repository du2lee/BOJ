N = int(input())
arr = list(map(int, input().split()))
count = 0

for i in arr:
    if N == i:
        count += 1

print(count)