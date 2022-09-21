arr = list(map(int, input().split()))
check = [False, False, False]

arr.sort()

if arr[0] == arr[1]:
    check[0] = True
    check[1] = True
if arr[0] == arr[2]:
    check[0] = True
    check[2] = True
if arr[1] == arr[2]:
    check[0] = True
    check[2] = True

if check[0] and check[1] and check[2]:
    print(10000 + arr[-1] * 1000)
elif check[1] and check[2]:
    print(1000 + arr[-1] * 100)
elif check[0] and check[2]:
    print(1000 + arr[-1] * 100)
elif check[1] and check[0]:
    print(1000 + arr[0] * 100)
else:
    print(arr[-1] * 100)