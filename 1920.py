N = int(input())

arr = set(map(int, input().split()))

M = int(input())

arr2 = list(map(int, input().split()))

for idx in arr2:
    if idx in arr:
        print(1)
    else:
        print(0)