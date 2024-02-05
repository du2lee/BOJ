N = int(input())

arr = {}

for _ in range(N):
    arr[input()] = True

for _ in range(N - 1):
    del(arr[input()])

print(list(arr.keys())[0])