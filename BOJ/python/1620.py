N, M = list(map(int, input().split()))

arr = dict()

for i in range(N):
    arr[input()] = i + 1

reverseArr = {v:k for k,v in arr.items()}

for _ in range(M):
    try:
        a = input()
        print(arr[a])
    except:
        print(reverseArr[int(a)])