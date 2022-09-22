N = int(input())

getArr = input().split()

M = int(input())
checkArr = input().split()
check = dict()

for i in checkArr:
    check[i] = 0

for i in getArr:
    try:
        check[i] += 1
    except:
        pass

for i in checkArr:
    print(check[i], end=' ')
print()