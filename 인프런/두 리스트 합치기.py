import math

N = int(input())
arr1 = list(map(int, input().split()))
M = int((input()))
arr2 = list(map(int, input().split()))

# 함수 값 들 비교하는 방법
a = arr1.pop(0)
b = arr2.pop(0)
while a != math.inf or b != math.inf:
    if a >= b:
        print(b, end = " ")
        b = math.inf
        if len(arr2) != 0:
            b = arr2.pop(0)
    else:
        print(a, end = " ")
        a = math.inf
        if len(arr1) != 0:
            a = arr1.pop(0)
    
# sort 함수 활용 방법
answer = arr1 + arr2
answer.sort()
for num in answer:
    print(num, end= " ")







